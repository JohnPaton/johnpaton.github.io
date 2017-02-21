# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1487708451.9328706
_enable_loop = True
_template_filename = 'themes/zen/templates/post.tmpl'
_template_uri = 'post.tmpl'
_source_encoding = 'utf-8'
_exports = ['content', 'extra_head']


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

    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
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
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        helper = _mako_get_namespace(context, 'helper')
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        arusahni = _mako_get_namespace(context, 'arusahni')
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

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
        arusahni = _mako_get_namespace(context, 'arusahni')
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    <div class="post">\n    ')
        __M_writer(str(arusahni.html_title()))
        __M_writer('\n        <div class="meta">\n            <div class="authordate">\n                <time class="timeago" datetime="')
        __M_writer(str(post.date.isoformat()))
        __M_writer('">')
        __M_writer(str(post.formatted_date(date_format)))
        __M_writer('</time>\n            ')
        __M_writer(str(arusahni.html_translations(post)))
        __M_writer('\n            ')
        __M_writer(str(arusahni.html_sourcelink()))
        __M_writer('\n            </div>\n            ')
        __M_writer(str(arusahni.html_tags(post)))
        __M_writer('\n        </div>\n        <div class="body">\n            ')
        __M_writer(str(post.text()))
        __M_writer('\n        </div>\n        ')
        __M_writer(str(helper.html_pager(post)))
        __M_writer('\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer('            ')
            __M_writer(str(comments.comment_form(post.permalink(absolute=True), post.title(), post._base_path)))
            __M_writer('\n')
        __M_writer('        ')
        __M_writer(str(helper.mathjax_script(post)))
        __M_writer('\n    </div>\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'arusahni')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        helper = _mako_get_namespace(context, 'helper')
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if post.meta('keywords'):
            __M_writer('        <meta name="keywords" content="')
            __M_writer(filters.html_escape(str(post.meta('keywords'))))
            __M_writer('">\n')
        __M_writer('    <meta name="author" content="')
        __M_writer(str(post.author()))
        __M_writer('">\n    ')
        __M_writer(str(helper.open_graph_metadata(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.twitter_card_information(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.meta_translations(post)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 7, "129": 8, "130": 8, "131": 9, "132": 10, "133": 10, "134": 10, "135": 12, "136": 12, "137": 12, "138": 13, "139": 13, "140": 14, "141": 14, "142": 15, "143": 15, "149": 143, "23": 4, "26": 2, "29": 3, "35": 0, "53": 2, "54": 3, "55": 4, "56": 5, "61": 16, "66": 39, "72": 18, "86": 18, "87": 20, "88": 20, "89": 23, "90": 23, "91": 23, "92": 23, "93": 24, "94": 24, "95": 25, "96": 25, "97": 27, "98": 27, "99": 30, "100": 30, "101": 32, "102": 32, "103": 33, "104": 34, "105": 34, "106": 34, "107": 36, "108": 36, "109": 36, "110": 38, "111": 38, "117": 7}, "uri": "post.tmpl", "filename": "themes/zen/templates/post.tmpl"}
__M_END_METADATA
"""
