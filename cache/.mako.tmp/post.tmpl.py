# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1494531910.5240664
_enable_loop = True
_template_filename = 'themes/zen/templates/post.tmpl'
_template_uri = 'post.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('arusahni', context._clean_inheritance_tokens(), templateuri='arusahni_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'arusahni')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

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
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        helper = _mako_get_namespace(context, 'helper')
        arusahni = _mako_get_namespace(context, 'arusahni')
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'arusahni')._populate(_import_ns, ['*'])
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        def extra_head():
            return render_extra_head(context)
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        helper = _mako_get_namespace(context, 'helper')
        __M_writer = context.writer()
        __M_writer('\r\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\r\n')
        if post.meta('keywords'):
            __M_writer('        <meta name="keywords" content="')
            __M_writer(filters.html_escape(str(post.meta('keywords'))))
            __M_writer('">\r\n')
        __M_writer('    <meta name="author" content="')
        __M_writer(str(post.author()))
        __M_writer('">\r\n    ')
        __M_writer(str(helper.open_graph_metadata(post)))
        __M_writer('\r\n    ')
        __M_writer(str(helper.twitter_card_information(post)))
        __M_writer('\r\n    ')
        __M_writer(str(helper.meta_translations(post)))
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'arusahni')._populate(_import_ns, ['*'])
        arusahni = _mako_get_namespace(context, 'arusahni')
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context)
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        helper = _mako_get_namespace(context, 'helper')
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="post">\r\n    ')
        __M_writer(str(arusahni.html_title()))
        __M_writer('\r\n        <div class="meta">\r\n            <div class="authordate">\r\n                <time class="timeago" datetime="')
        __M_writer(str(post.date.isoformat()))
        __M_writer('">')
        __M_writer(str(post.formatted_date(date_format)))
        __M_writer('</time>\r\n            ')
        __M_writer(str(arusahni.html_translations(post)))
        __M_writer('\r\n            ')
        __M_writer(str(arusahni.html_sourcelink()))
        __M_writer('\r\n            </div>\r\n            ')
        __M_writer(str(arusahni.html_tags(post)))
        __M_writer('\r\n        </div>\r\n        <div class="body">\r\n            ')
        __M_writer(str(post.text()))
        __M_writer('\r\n        </div>\r\n        ')
        __M_writer(str(helper.html_pager(post)))
        __M_writer('\r\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer('            ')
            __M_writer(str(comments.comment_form(post.permalink(absolute=True), post.title(), post._base_path)))
            __M_writer('\r\n')
        __M_writer('        ')
        __M_writer(str(helper.mathjax_script(post)))
        __M_writer('\r\n    </div>\r\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "post.tmpl", "filename": "themes/zen/templates/post.tmpl", "line_map": {"128": 25, "129": 27, "130": 27, "131": 30, "132": 30, "133": 32, "134": 32, "135": 33, "136": 34, "137": 34, "138": 34, "139": 36, "140": 36, "141": 36, "142": 38, "143": 38, "149": 143, "23": 2, "26": 4, "29": 3, "35": 0, "53": 2, "54": 3, "55": 4, "56": 5, "61": 16, "66": 39, "72": 7, "83": 7, "84": 8, "85": 8, "86": 9, "87": 10, "88": 10, "89": 10, "90": 12, "91": 12, "92": 12, "93": 13, "94": 13, "95": 14, "96": 14, "97": 15, "98": 15, "104": 18, "118": 18, "119": 20, "120": 20, "121": 23, "122": 23, "123": 23, "124": 23, "125": 24, "126": 24, "127": 25}}
__M_END_METADATA
"""