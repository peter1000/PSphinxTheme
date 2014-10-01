"""
.. index:: Extensions; issue_tracker

==============================
PSphinxTheme.ext.issue_tracker
==============================

Overview
========
**support for `issue` text role**

This Sphinx extension adds a new text role, ``:issue:``, which will automatically be converted into links to your project's
issue tracker.

Issue roles should have the format ``:issue:`5``` or ``:issue:`Custom Title <5>```.
They will be converted into external references to the appropriate issue number in your project's issue tracker.


Configuration
=============
This extension reads the following ``conf.py`` options:

   ``issue_tracker_url``

      This should provide a path to the project's issue tracker. It should have one of the following formats:

      * :samp:`bb:{user}/{project}` -- link to BitBucket issue tracker for specified project
      * :samp:`gh:{user}/{project}` -- link to GitHub issue tracker for specified project
      * :samp:`gc:{project}` -- link to Google Code issue tracker for specified project
      * string containing arbitrary url, the substring ``{issue}`` will be replaced with the relevant issue number, and
         ``{title}`` with the link title.

      If this option is not specified, all issue references will be converted into labels instead of links.

   ``issue_tracker_title``

      Template for generating default title for references that only specify the issue number (e.g. ``:issue:`5```).
      This defaults to ``Issue {issue}``.


.. index:: Usage; extension: issue_tracker usage example

``conf.py`` Usage Example::

   # add to list of extensions:
   extensions = [
      ...
      'PSphinxTheme.ext.issue_tracker',
   ]

   ...

   # set path to issue tracker:
   issue_tracker_url = "https://example.org/tracker/{issue}"


Internals
=========
.. note::

   For themeing purposes, the generated ``<a>`` tag will have an ``issue`` CSS class added to it.
"""
# ===========================================================================================================================
# imports
# ===========================================================================================================================
# noinspection PyPep8Naming
from re import (
   compile as re_compile,
   X as re_X,
)

from docutils import nodes
from docutils.parsers.rst.roles import set_classes


# ===========================================================================================================================
# issue role
# ===========================================================================================================================
def make_error(inliner, rawtext, line, value):
   """ generate error node and msg
   """
   msg = inliner.reporter.error(value, line=line)
   node = inliner.problematic(rawtext, rawtext, msg)
   return [node], [msg]


def get_issue_tracker_title(config):
   """ retrieve issue_tracker_title template
   """
   return getattr(config, 'issue_tracker_title', None) or 'issue {issue}'


def get_issue_tracker_url(config):
   """ retrieve issue_tracker_url template, replacing aliases
   """
   template = getattr(config, 'issue_tracker_url', None)
   if not template:
      # causes :issue:`xx` to be replaced with label instead of url.
      return None

   elif template.startswith('bb:'):
      # parse 'bb:<project>', and replace with bitbucket url
      project = template[3:].strip('/')
      return 'https://bitbucket.org/' + project + '/issue/{issue}'

   elif template.startswith('gc:'):
      # parse 'gc:<project>', and replace with google code url
      project = template[3:].strip('/')
      return 'https://code.google.com/p/' + project + \
             '/issues/detail?id={issue}'

   elif template.startswith('gh:'):
      # parse 'gh:<project>', and replace with github url
      project = template[3:].strip('/')
      return 'https://github.com/' + project + '/issues/{issue}'

   else:
      # assume it contains {issue} and possibly {title}
      return template

# pattern allows inside :issue: text roles
issue_re = re_compile('''
    ^
    (?:
        (?P<title>[^<]+)
        \s*
        <
        (?P<issue1>\d+)
        >
    |
        (?P<issue2>\d+)
    )
    $
    ''', re_X)


# noinspection PyUnusedLocal,PyDefaultArgument
def issue_role(name, rawtext, text, line, inliner, options={}, content=[]):
   """ generate link to an issue
   """
   # NOTE:
   #   name - role name in doc, should be 'issue'
   #   rawtext - text of entire node
   #   text - contents of role
   #   lineno
   #   inliner - ???
   #   options - ???
   #   content - ???
   # returns (nodes, messages)

   # extract title & issue number from text
   m_ = issue_re.match(text)
   if m_:
      issue = int(m_.group('issue1') or m_.group('issue2'))
      title = m_.group('title')
   else:
      return make_error(inliner, rawtext, line, 'Invalid issue identifier: %r' % (text,))

   # get url template from config, resolve aliases
   config = inliner.document.settings.env.app.config
   url_template = get_issue_tracker_url(config)
   title_template = get_issue_tracker_title(config)

   # generate replacement node
   if not title:
      title = title_template.format(issue=issue)
   set_classes(options)
   clist = options.setdefault('classes', [])
   clist.append('issue')
   if url_template:
      url = url_template.format(issue=issue, title=title)
      node = nodes.reference(rawtext, title, refuri=url, **options)
   else:
      node = nodes.emphasis(rawtext, title, **options)
   return [node], []


# ===========================================================================================================================
# init
# ===========================================================================================================================

def setup(app):
   """ register extension
   """
   app.add_config_value('issue_tracker_url', None, 'env')
   app.add_config_value('issue_tracker_title', None, 'env')
   app.add_role('issue', issue_role)

# ===========================================================================================================================
# eof
# ===========================================================================================================================
