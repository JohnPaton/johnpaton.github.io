# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1487708451.472063
_enable_loop = True
_template_filename = 'themes/zen/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('arusahni', context._clean_inheritance_tokens(), templateuri='arusahni_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'arusahni')] = ns

    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'arusahni')._populate(_import_ns, ['*'])
        def content():
            return render_content(context._locals(__M_locals))
        comments = _mako_get_namespace(context, 'comments')
        helper = _mako_get_namespace(context, 'helper')
        index_teasers = _import_ns.get('index_teasers', context.get('index_teasers', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        arusahni = _mako_get_namespace(context, 'arusahni')
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'arusahni')._populate(_import_ns, ['*'])
        def content():
            return render_content(context)
        comments = _mako_get_namespace(context, 'comments')
        helper = _mako_get_namespace(context, 'helper')
        index_teasers = _import_ns.get('index_teasers', context.get('index_teasers', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        arusahni = _mako_get_namespace(context, 'arusahni')
        __M_writer = context.writer()
        __M_writer('\n')
        for post in posts:
            __M_writer('        <div class="post">\n            <h1 class="title"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('">')
            __M_writer(str(post.title()))
            __M_writer('</a></h1>\n            <div class="meta">\n                <div class="authordate">\n                    <time class="timeago" datetime="')
            __M_writer(str(post.date.isoformat()))
            __M_writer('">')
            __M_writer(str(post.formatted_date(date_format)))
            __M_writer('</time>\n                </div>\n                <div class="stats">\n')
            if not post.meta('nocomments'):
                __M_writer('                    ')
                __M_writer(str(comments.comment_link(post.permalink(), post.base_path)))
                __M_writer('\n')
            __M_writer('                </div>\n            ')
            __M_writer(str(arusahni.html_tags(post)))
            __M_writer('\n            </div>\n            <div class="body">\n')
            if index_teasers:
                __M_writer('                ')
                __M_writer(str(post.text(teaser_only=True)))
                __M_writer('\n')
            else:
                __M_writer('                ')
                __M_writer(str(post.text(teaser_only=False)))
                __M_writer('\n')
            __M_writer('            </div>\n        </div>\n')
        __M_writer('    ')
        __M_writer(str(helper.html_pager()))
        __M_writer('\n    ')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n    ')
        __M_writer(str(helper.mathjax_script(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"23": 4, "26": 2, "29": 3, "35": 0, "50": 2, "51": 3, "52": 4, "53": 5, "58": 34, "64": 7, "78": 7, "79": 8, "80": 9, "81": 10, "82": 10, "83": 10, "84": 10, "85": 13, "86": 13, "87": 13, "88": 13, "89": 16, "90": 17, "91": 17, "92": 17, "93": 19, "94": 20, "95": 20, "96": 23, "97": 24, "98": 24, "99": 24, "100": 25, "101": 26, "102": 26, "103": 26, "104": 28, "105": 31, "106": 31, "107": 31, "108": 32, "109": 32, "110": 33, "111": 33, "117": 111}, "uri": "index.tmpl", "filename": "themes/zen/templates/index.tmpl"}
__M_END_METADATA
"""
