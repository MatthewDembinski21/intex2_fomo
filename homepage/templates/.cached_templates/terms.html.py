# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520526928.275338
_enable_loop = True
_template_filename = 'C:/Users/mayaroney/desktop/fomo/homepage/templates/terms.html'
_template_uri = 'terms.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['top_center', 'content_center']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'app_base.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def top_center():
            return render_top_center(context._locals(__M_locals))
        def content_center():
            return render_content_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_center'):
            context['self'].top_center(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_center'):
            context['self'].content_center(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_center():
            return render_top_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n<h1>Terms & Conditions</h1>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_center():
            return render_content_center(context)
        __M_writer = context.writer()
        __M_writer("\r\n\r\n\r\n\r\n\r\n<p>\r\n    These terms and conditions govern your use of this website; by using this website, you accept these terms and conditions in full.   If you disagree with these terms and conditions or any part of these terms and conditions, you must not use this website.\r\n\r\n[You must be at least [18] years of age to use this website.  By using this website [and by agreeing to these terms and conditions] you warrant and represent that you are at least [18] years of age.]\r\n\r\n[This website uses cookies.  By using this website and agreeing to these terms and conditions, you consent to our [NAME]'s use of cookies in accordance with the terms of [NAME]'s [privacy policy / cookies policy].]\r\n</p>\r\n\r\n<h3>License to use website</h3>\r\n<p>\r\nUnless otherwise stated, [NAME] and/or its licensors own the intellectual property rights in the website and material on the website.  Subject to the license below, all these intellectual property rights are reserved.\r\n<br/>\r\nYou may view, download for caching purposes only, and print pages [or [OTHER CONTENT]] from the website for your own personal use, subject to the restrictions set out below and elsewhere in these terms and conditions.\r\n<br/>\r\nYou must not:\r\n<ul>\r\n    <li>republish material from this website (including republication on another website);</li>\r\n    <li>sell, rent or sub-license material from the website;</li>\r\n    <li>show any material from the website in public;</li>\r\n    <li>reproduce, duplicate, copy or otherwise exploit material on this website for a commercial purpose;]</li>\r\n    <li>[edit or otherwise modify any material on the website; or]</li>\r\n    <li>[redistribute material from this website [except for content specifically and expressly made available for redistribution].]</li>\r\n</ul>\r\n<br/>\r\n[Where content is specifically made available for redistribution, it may only be redistributed [within your organisation].]\r\n</p>\r\n\r\n<h3>Acceptable use</h3>\r\n\r\n<p>\r\n    You must not use this website in any way that causes, or may cause, damage to the website or impairment of the availability or accessibility of the website; or in any way which is unlawful, illegal, fraudulent or harmful, or in connection with any unlawful, illegal, fraudulent or harmful purpose or activity.\r\n<br/>\r\n    You must not use this website to copy, store, host, transmit, send, use, publish or distribute any material which consists of (or is linked to) any spyware, computer virus, Trojan horse, worm, keystroke logger, rootkit or other malicious computer software.\r\n<br/>\r\n    You must not conduct any systematic or automated data collection activities (including without limitation scraping, data mining, data extraction and data harvesting) on or in relation to this website without [NAME'S] express written consent.\r\n<br/>\r\n    [You must not use this website to transmit or send unsolicited commercial communications.]\r\n<br/>\r\n    [You must not use this website for any purposes related to marketing without [NAME'S] express written consent.]\r\n</p>\r\n\r\n<h3>Restricted access</h3>\r\n<p>\r\n[Access to certain areas of this website is restricted.]  [NAME] reserves the right to restrict access to [other] areas of this website, or indeed this entire website, at [NAME'S] discretion.\r\n<br/>\r\nIf [NAME] provides you with a user ID and password to enable you to access restricted areas of this website or other content or services, you must ensure that the user ID and password are kept confidential.\r\n<br/>\r\n[[NAME] may disable your user ID and password in [NAME'S] sole discretion without notice or explanation.]\r\n</p><br/>\r\n\r\n<h3>User content</h3>\r\n<p>\r\nIn these terms and conditions, “your user content” means material (including without limitation text, images, audio material, video material and audio-visual material) that you submit to this website, for whatever purpose.\r\n<br/>\r\nYou grant to [NAME] a worldwide, irrevocable, non-exclusive, royalty-free license to use, reproduce, adapt, publish, translate and distribute your user content in any existing or future media.  You also grant to [NAME] the right to sub-license these rights, and the right to bring an action for infringement of these rights.\r\n<br/>\r\nYour user content must not be illegal or unlawful, must not infringe any third party's legal rights, and must not be capable of giving rise to legal action whether against you or [NAME] or a third party (in each case under any applicable law).\r\n<br/>\r\nYou must not submit any user content to the website that is or has ever been the subject of any threatened or actual legal proceedings or other similar complaint.\r\n<br/>\r\n[NAME] reserves the right to edit or remove any material submitted to this website, or stored on [NAME'S] servers, or hosted or published upon this website.\r\n<br/>\r\n[Notwithstanding [NAME'S] rights under these terms and conditions in relation to user content, [NAME] does not undertake to monitor the submission of such content to, or the publication of such content on, this website.]\r\n</p><br/>\r\n\r\n<h3>No warranties</h3>\r\n<p>\r\nThis website is provided “as is” without any representations or warranties, express or implied.  [NAME] makes no representations or warranties in relation to this website or the information and materials provided on this website.\r\n<br/>\r\nWithout prejudice to the generality of the foregoing paragraph, [NAME] does not warrant that:\r\n<br/>\r\n\uf06c\tthis website will be constantly available, or available at all; or\r\n\uf06c\tthe information on this website is complete, true, accurate or non-misleading.\r\n<br/>\r\nNothing on this website constitutes, or is meant to constitute, advice of any kind.  [If you require advice in relation to any [legal, financial or medical] matter you should consult an appropriate professional.]\r\n</p><br/>\r\n\r\n<h3>Limitations of liability</h3>\r\n\r\n[NAME] will not be liable to you (whether under the law of contact, the law of torts or otherwise) in relation to the contents of, or use of, or otherwise in connection with, this website:\r\n\r\n\uf06c\t[to the extent that the website is provided free-of-charge, for any direct loss;]\r\n\uf06c\tfor any indirect, special or consequential loss; or\r\n\uf06c\tfor any business losses, loss of revenue, income, profits or anticipated savings, loss of contracts or business relationships, loss of reputation or goodwill, or loss or corruption of information or data.\r\n\r\nThese limitations of liability apply even if [NAME] has been expressly advised of the potential loss.\r\n\r\nExceptions\r\n\r\nNothing in this website disclaimer will exclude or limit any warranty implied by law that it would be unlawful to exclude or limit; and nothing in this website disclaimer will exclude or limit [NAME'S] liability in respect of any:\r\n\r\n\uf06c\tdeath or personal injury caused by [NAME'S] negligence;\r\n\uf06c\tfraud or fraudulent misrepresentation on the part of [NAME]; or\r\n\uf06c\tmatter which it would be illegal or unlawful for [NAME] to exclude or limit, or to attempt or purport to exclude or limit, its liability.\r\n\r\nReasonableness\r\n\r\nBy using this website, you agree that the exclusions and limitations of liability set out in this website disclaimer are reasonable.\r\n\r\nIf you do not think they are reasonable, you must not use this website.\r\n\r\nOther parties\r\n\r\n[You accept that, as a limited liability entity, [NAME] has an interest in limiting the personal liability of its officers and employees.  You agree that you will not bring any claim personally against [NAME'S] officers or employees in respect of any losses you suffer in connection with the website.]\r\n\r\n[Without prejudice to the foregoing paragraph,] you agree that the limitations of warranties and liability set out in this website disclaimer will protect [NAME'S] officers, employees, agents, subsidiaries, successors, assigns and sub-contractors as well as [NAME].\r\n\r\nUnenforceable provisions\r\n\r\nIf any provision of this website disclaimer is, or is found to be, unenforceable under applicable law, that will not affect the enforceability of the other provisions of this website disclaimer.\r\n\r\nIndemnity\r\n\r\nYou hereby indemnify [NAME] and undertake to keep [NAME] indemnified against any losses, damages, costs, liabilities and expenses (including without limitation legal expenses and any amounts paid by [NAME] to a third party in settlement of a claim or dispute on the advice of [NAME'S] legal advisers) incurred or suffered by [NAME] arising out of any breach by you of any provision of these terms and conditions[, or arising out of any claim that you have breached any provision of these terms and conditions].\r\n\r\nBreaches of these terms and conditions\r\n\r\nWithout prejudice to [NAME'S] other rights under these terms and conditions, if you breach these terms and conditions in any way, [NAME] may take such action as [NAME] deems appropriate to deal with the breach, including suspending your access to the website, prohibiting you from accessing the website, blocking computers using your IP address from accessing the website, contacting your internet service provider to request that they block your access to the website and/or bringing court proceedings against you.\r\n\r\nVariation\r\n\r\n[NAME] may revise these terms and conditions from time-to-time.  Revised terms and conditions will apply to the use of this website from the date of the publication of the revised terms and conditions on this website.  Please check this page regularly to ensure you are familiar with the current version.\r\n\r\nAssignment\r\n\r\n[NAME] may transfer, sub-contract or otherwise deal with [NAME'S] rights and/or obligations under these terms and conditions without notifying you or obtaining your consent.\r\n\r\nYou may not transfer, sub-contract or otherwise deal with your rights and/or obligations under these terms and conditions.\r\n\r\nSeverability\r\n\r\nIf a provision of these terms and conditions is determined by any court or other competent authority to be unlawful and/or unenforceable, the other provisions will continue in effect.  If any unlawful and/or unenforceable provision would be lawful or enforceable if part of it were deleted, that part will be deemed to be deleted, and the rest of the provision will continue in effect.\r\n\r\nEntire agreement\r\n\r\nThese terms and conditions [, together with [DOCUMENTS],] constitute the entire agreement between you and [NAME] in relation to your use of this website, and supersede all previous agreements in respect of your use of this website.\r\n\r\nLaw and jurisdiction\r\n\r\nThese terms and conditions will be governed by and construed in accordance with [GOVERNING LAW], and any disputes relating to these terms and conditions will be subject to the [non-]exclusive jurisdiction of the courts of [JURISDICTION].\r\n\r\nCredit: This document was created using a Contractology template available at http://www.contractology.com.\r\n\r\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/mayaroney/desktop/fomo/homepage/templates/terms.html", "uri": "terms.html", "source_encoding": "utf-8", "line_map": {"29": 0, "38": 1, "43": 5, "48": 155, "54": 3, "60": 3, "66": 7, "72": 7, "78": 72}}
__M_END_METADATA
"""
