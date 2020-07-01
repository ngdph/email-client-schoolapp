# tset = """<!DOCTYPE html>
# <html>
# <head>
# <meta http-equiv=3D"Content-Type" content=3D"text/html; charset=3DUTF-8" />
# <!--[if !mso]><!-->
# <meta http-equiv=3D"X-UA-Compatible" content=3D"IE=3Dedge" />
# <!--<![endif]-->=20
# <meta name=3D"viewport" content=3D"width=3Ddevice-width, initial-scale=3D1"=
#  />
# <meta name=3D"x-apple-disable-message-reformatting" />
# <!--[if gte mso 9]>
# <xml>
# <o:OfficeDocumentSettings>
# <o:AllowPNG/>
# <o:PixelsPerInch>96</o:PixelsPerInch>
# </o:OfficeDocumentSettings>
# </xml>
# <![endif]-->
# <title></title>
# <style type=3D"text/css">
# <!--
# #outlook a { padding: 0; }
# .text-block table { mso-table-rspace: 10pt; }
# .ReadMsgBody { width: 100%; background-color: #ffffff }
# .ExternalClass { width: 100%; background-color: #ffffff }
# .ExternalClass * { line-height: 100% !important; }
# html, body { margin: 0 auto !important; padding: 0 !important; height: 100%=
#  !important; width: 100% !important; background-color: #ffffff; -webkit-fon=
# t-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; transform: sc=
# ale(1, 1); zoom: 1; }
# * { -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; }
# div[style*=3D"margin: 16px 0"] { margin: 0 !important; }
# .wrap { table-layout: fixed; width: 100% !important; padding: 0px; margin: =
# 0px; }
# .wrap img {-ms-interpolation-mode: bicubic;margin: 0 !important;padding: 0 =
# !important;-webkit-box-sizing: border-box;-moz-box-sizing: border-box;box-s=
# izing: border-box;font-size: 12px}
# .wrap [data-editable=3D"image"] img {display: block;}
# .wrap ul {list-style-position: outside;}
# table font {background-color: inherit;}
# .wrap table {border-collapse: collapse;border-spacing: 0px;padding: 0px;emp=
# ty-cells: hide;-webkit-font-smoothing: antialiased;-moz-osx-font-smoothing:=
#  grayscale;}
# .wrap table * {-webkit-font-smoothing: antialiased;-moz-osx-font-smoothing:=
#  grayscale;}
# .wrap tr {font-size: 0;border-collapse: collapse;border-spacing: 0px;}
# .wrap td {display: table-cell !important;border-collapse: collapse;border-s=
# pacing: 0px;}
# .wrap td.column {display: table-cell !important;min-width: auto;max-width: =
# auto;float: none !important;}
# .wrap td.tdBlock {display: inline-block !important;}
# body[data-getresponse] td[class=3D"column"] {display: table-cell !important=
# ;float: none !important;min-width: auto;max-width: auto;}
# table[data-editable=3D"image"] + ul {list-style-position: inside;}
# @media all and (max-width: 480px) {
# .abandonedcart-product-cell {display: block !important;width: 100% !importa=
# nt;vertical-align: top;text-align: center !important;}
# .abandonedcart-product-cell table {width: 100% !important;}
# .abandonedcart-image-placeholder {width: 100% !important;}
# .abandonedcart-product-cell > table {width: 100% !important;}
# [data-editable=3D"abandonedcart-product"] td,[data-editable=3D"abandonedcar=
# t-price"] td {text-align: center !important;width: 100% !important;}
# .ecommerce-products-cell {display: block !important;width: 100% !important;=
# vertical-align: top;}
# .ecommerce-image-placeholder {width: 100% !important;}
# .ecommerce-products-cell > table {width: 100% !important;}
# div.wrap > div {width: 100% !important;}body {-webkit-box-sizing: border-bo=
# x;-moz-box-sizing: border-box;box-sizing: border-box;}
# .wrap table {-webkit-box-sizing: border-box;-moz-box-sizing: border-box;box=
# -sizing: border-box;}
# table[class=3D"column-full-width"] { width: 100% !important; }table td {-we=
# bkit-box-sizing: border-box;-moz-box-sizing: border-box;box-sizing: border-=
# box;}
# div[class=3D"WRAPPER"] {max-width: 100% !important;width: 100% !important;}
# table td[class=3D"column"] {display: block;max-width: 100% !important;width=
# : auto !important;}
# table[data-editable=3D"rss"] table { padding: 5px 10px !important; }
# div[class=3D"column"] { width: 100% !important; max-width: 100% !important;=
#  }
# .column { display: block !important; width: 100% !important; max-width: 100=
# % !important; }}
# .pl_image, .outline .editable .imagemask div {vertical-align: middle;text-a=
# lign: center;font-family: Arial,Helvetica,sans-serif;color: #ffffff;font-si=
# ze: 20px;-webkit-border-radius: 6px;-moz-border-radius: 6px;border-radius: =
# 6px;background: #dedede url(https://www.getresponse.com/images/common/templ=
# ates/messages/elements/placeholders/image.png) no-repeat 50% 50%;width: 100=
# %;height: 100%;overflow: hidden;}
# .ecommerce-image-placeholder {
# width: 270px;
# height: 150px;
# background: #dedede url(/images/common/templates/messages/elements/placehol=
# ders/image.png) no-repeat 50% 70%;
# }
# .ecommerce-products-cell, [data-editable=3D"ecommerce"] .column {
# padding-bottom: 25px;
# }
# .ecommerce-button-row td {
# padding-top: 10px;
# }
# .ecommerce-button-container td {max-width: 270px;word-break: break-all;}.ab=
# andonedcart-image-placeholder {
# width: 200px;
# height: 117px;
# background: #dedede url(/images/common/templates/messages/elements/placehol=
# ders/image.png) no-repeat 50% 70%;
# }
# .abandonedcart-product-cell {
# padding-bottom: 15px;
# }
# .abandonedcart-cta-container {
# padding-bottom: 15px;
# }
# .abandonedcart-cta-container td {
# max-width: 270px;
# word-break: break-all;
# }
# [data-editable=3D"abandonedcart-product"],[data-editable=3D"abandonedcart-p=
# rice"] {width: 100%;}
# [data-editable=3D"abandonedcart-button"] a {text-decoration: none;}.product=
# box-image-placeholder {
#     width: 100%;
#     height: 150px;
#     background: #dedede url(/images/common/templates/messages/elements/plac=
# eholders/image.png) no-repeat 50% 70%;
# }
# .productbox-product-cell {
#     padding-bottom: 15px;
#     vertical-align: top;
#     position: relative;
#     z-index: 2;
# }

# .productbox-button-row .productbox-button-container {
#     padding-top: 10px;
# }

# .productbox-button-container td {
#     max-width: 270px;
#     word-break: break-all;
# }.funnel-product-cell {
# padding-bottom: 45px;
# }
# .funnel-button-row td {
# padding-top: 10px;
# }
# .funnel-button-container td {max-width: 270px;word-break: break-all;}
# .funnel-product-details {width: 358px;padding-left: 5px;}--></style>

# </head>
# <body data-getresponse=3D"true" style=3D"margin: 0; padding: 0;">
# <div class=3D"wrap" style=3D"width: 100%; min-width: 320px; table-layout: f=
# ixed; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%;"><style t=
# ype=3D"text/css"><!-- table[class=3D"wrapper"] {width: undefinedpx;max-widt=
# h: undefinedpx !important;font-size: 16px;}
# td[class=3D"column"] { min-width: 0 !important; }=20
# body[data-getresponse] td[class=3D"column"] { float: none !important; }body=
# [xx-iframe] td[class=3D"column"] { display: table-cell !important; float: n=
# one !important; }--></style>
# <table data-mobile=3D"false" width=3D"100%" cellpadding=3D"0" cellspacing=
# =3D"0" border=3D"0" dir=3D"ltr" align=3D"center" data-width=3D"600" style=
# =3D"background-color: rgb(255, 255, 255);">

#     <tbody>

#         <tr>

#             <td align=3D"left" valign=3D"top" style=3D"margin: 0; padding: =
# 0;" class=3D"responsive-cell">

#                 <table align=3D"center" border=3D"0" cellspacing=3D"0" cell=
# padding=3D"0" width=3D"600" bgcolor=3D"#ffffff" class=3D"wrapper" style=3D"=
# background-image: none; width: 600px;">

#                     <tbody>

#                        =20

#                         <tr><td align=3D"center" valign=3D"top" style=3D"ma=
# rgin: 0px; padding: 0px;" class=3D"responsive-cell"><table width=3D"100%" b=
# order=3D"0" cellpadding=3D"0" cellspacing=3D"0" align=3D"center" data-edita=
# ble=3D"text" class=3D"text-block"><tbody><tr><td align=3D"left" valign=3D"t=
# op" class=3D"lh-1" style=3D"padding: 3px; font-size: 10px; font-family: 'Ti=
# mes New Roman', Times, serif; line-height: 1.15;"><span style=3D"color: rgb=
# (128, 128, 128); font-family: Helvetica,'Helvetica Neue', Arial, sans-serif=
# ; font-size: 9px; font-style: italic;">Apple ch=C3=ADnh h=C3=A3ng gi=C3=A1 =
# r=E1=BA=BB v=C3=B4 =C4=91=E1=BB=8Bch - Y=C3=AAn t=C3=A2m b=E1=BA=A3o h=C3=
# =A0nh ch=C3=ADnh h=C3=A3ng</span></td></tr></tbody></table></td></tr>

#                         <tr><td align=3D"center" valign=3D"top" style=3D"ma=
# rgin: 0px; padding: 0px;" class=3D"responsive-cell"><table cellpadding=3D"0=
# " cellspacing=3D"0" align=3D"center" data-editable=3D"image" data-mobile-st=
# retch=3D"1" style=3D"" width=3D"100%">

#                                     <tbody>

#                                         <tr>

#                                             <td valign=3D"top" align=3D"lef=
# t" style=3D"display: inline-block; padding: 0px; margin: 0px;" class=3D"tdB=
# lock responsive-cell"><a href=3D"https://inmail.inone.useinsider.com/click.=
# html?x=3Da62e&lc=3D81tS&mc=3Du&s=3DksNEG&u=3DFt&z=3DcgMLqBK&" target=3D"_bl=
# ank"><img createnew=3D"true" src=3D"https://multimedia.inmail.inone.useinsi=
# der.com/insider-BU/photos/6d7c71ef-b705-4399-bb25-6320ea731ff2.jpg?img15930=
# 81522304" width=3D"609" data-src=3D"https://multimedia.inmail.inone.useinsi=
# der.com/insider-BU/photos/6d7c71ef-b705-4399-bb25-6320ea731ff2.jpg|609|88|6=
# 09|90|0|0|1" data-origsrc=3D"https://multimedia.inmail.inone.useinsider.com=
# /insider-BU/photos/e5904284-9f94-406e-927f-4e1fef78b82b.jpg" class=3D"mobil=
# e-image-stretch-enabled" style=3D"border-width: 0px; border-style: none; bo=
# rder-color: transparent; font-size: 12px; display: block; width: 100%; max-=
# width: 100% !important;"></a></td>

#                                         </tr>

#                                     </tbody>

#                                 </table></td></tr><tr><td align=3D"center" =
# valign=3D"top" style=3D"margin: 0px; padding: 0px;" class=3D"responsive-cel=
# l"><table cellpadding=3D"0" cellspacing=3D"0" align=3D"center" data-editabl=
# e=3D"image" data-mobile-stretch=3D"0" style=3D"max-width: 609px;">

#                                     <tbody>

#                                         <tr>

#                                             <td valign=3D"top" align=3D"lef=
# t" style=3D"display: inline-block; padding: 10px 0px 0px; margin: 0px;" cla=
# ss=3D"tdBlock responsive-cell"><a href=3D"https://inmail.inone.useinsider.c=
# om/click.html?x=3Da62e&lc=3D81to&mc=3Du&s=3DksNEG&u=3DFt&z=3DckVDmWC&" targ=
# et=3D"_blank"><img src=3D"https://multimedia.inmail.inone.useinsider.com/in=
# sider-BU/photos/6965632f-4e42-43b5-8edd-38bbe40a4172.png?img1593081522304" =
# width=3D"609" data-src=3D"https://multimedia.inmail.inone.useinsider.com/in=
# sider-BU/photos/6965632f-4e42-43b5-8edd-38bbe40a4172.png|609|305|609|305|0|=
# 0|1" height=3D"305" data-origsrc=3D"https://multimedia.inmail.inone.useinsi=
# der.com/insider-BU/photos/ef28e089-6193-4347-a2a7-4d341566b2af.png" class=
# =3D"mobile-image-stretch-disabled" style=3D"border-width: 0px; border-style=
# : none; border-color: transparent; font-size: 12px; display: block;"></a></=
# td>

#                                         </tr>

#                                     </tbody>

#                                 </table></td></tr>

#                        =20

#                         <tr>

#                             <td align=3D"center" valign=3D"top" style=3D"ma=
# rgin: 0px; padding: 0px;" class=3D"responsive-cell">

#                                 <table cellpadding=3D"0" cellspacing=3D"0" =
# border=3D"0" width=3D"100%">

#                                     <tbody>

#                                         <tr>

#                                             <td valign=3D"top" align=3D"lef=
# t" width=3D"33%" style=3D"padding: 0px; margin: 0px;" class=3D"responsive-c=
# ell">

#                                                 <table cellpadding=3D"0" ce=
# llspacing=3D"0" border=3D"0" width=3D"100%">

#                                                     <tbody>

#                                                         <tr><td align=3D"ce=
# nter" valign=3D"top" style=3D"margin: 0px; padding: 0px;" class=3D"responsi=
# ve-cell"><table cellpadding=3D"0" cellspacing=3D"0" align=3D"center" data-e=
# ditable=3D"image" data-mobile-stretch=3D"1" width=3D"100%"><tbody><tr><td v=
# align=3D"top" align=3D"center" style=3D"display: inline-block; padding: 10p=
# x 0px; margin: 0px;" class=3D"tdBlock responsive-cell"><a href=3D"https://i=
# nmail.inone.useinsider.com/click.html?x=3Da62e&lc=3D81tg&mc=3Du&s=3DksNEG&u=
# =3DFt&z=3Dco6uX4z&" target=3D"_blank"><img src=3D"https://multimedia.inmail=
# .inone.useinsider.com/insider-BU/photos/bcdf9427-b9d6-4776-a67e-8946d4c593b=
# 3.jpg?img1593081522304" width=3D"203" data-src=3D"https://multimedia.inmail=
# .inone.useinsider.com/insider-BU/photos/bcdf9427-b9d6-4776-a67e-8946d4c593b=
# 3.jpg|203|203|203|203|0|0|1" height=3D"203" data-origsrc=3D"https://multime=
# dia.inmail.inone.useinsider.com/insider-BU/photos/c99c8c7a-dfa2-410b-98b9-d=
# 6b497b54c9e.jpg" class=3D"mobile-image-stretch-enabled" style=3D"border-wid=
# th: 0px; border-style: none; border-color: transparent; font-size: 12px; di=
# splay: block;"></a></td></tr></tbody></table></td></tr>

#                                                         <tr><td align=3D"ce=
# nter" valign=3D"top" style=3D"margin: 0px; padding: 0px;" class=3D"responsi=
# ve-cell"><table width=3D"100%" border=3D"0" cellpadding=3D"0" cellspacing=
# =3D"0" align=3D"center" data-editable=3D"text" class=3D"text-block"><tbody>=
# <tr><td align=3D"left" valign=3D"top" class=3D"lh-3" style=3D"padding: 10px=
# ; font-size: 16px; font-family: 'Times New Roman', Times, serif; line-heigh=
# t: 1.35;"><span style=3D"font-family: Arial,'Helvetica Neue', Helvetica, sa=
# ns-serif; font-size: 17px; font-weight: 700;">Active 3 6GB</span><br><div c=
# lass=3D"responsive-cell" style=3D"padding: 0px;"><div><font style=3D"font-s=
# ize: 17px;"><span style=3D"font-family: Arial,'Helvetica Neue', Helvetica, =
# sans-serif; font-weight: bold; background-color: transparent;"><br></span><=
# /font></div><div><font style=3D"font-size: 12px;" size=3D"12"><span style=
# =3D"font-family: Arial,'Helvetica Neue', Helvetica, sans-serif; background-=
# color: transparent; text-decoration: line-through;">3.990.000=C4=91</span><=
# /font></div><div><span style=3D"background-color: transparent; font-family:=
#  Arial,'Helvetica Neue', Helvetica, sans-serif; font-weight: bold; color: r=
# gb(255, 0, 0);"><font style=3D"font-size: 23px;" size=3D"23">3.590.000</fon=
# t></span></div><div data-box=3D"button" style=3D"width: 100%; margin-top: 0=
# px; margin-bottom: 0px; text-align: left;"><table border=3D"0" cellpadding=
# =3D"0" cellspacing=3D"0" align=3D"left" data-editable=3D"button" style=3D"m=
# argin: 0px auto 0px 0px;"><tbody><tr><td valign=3D"top" align=3D"center" cl=
# ass=3D"tdBlock" style=3D"display: inline-block; padding: 3px 10px 3px 5px; =
# margin: 0px; background-color: rgb(255, 0, 0); border-radius: 1px;"><a href=
# =3D"https://inmail.inone.useinsider.com/click.html?x=3Da62e&lc=3D81tg&mc=3D=
# u&s=3DksNEG&u=3DFt&z=3Dcu1MknK&" style=3D"font-family: Arial,'Helvetica Neu=
# e', Helvetica, sans-serif; color: rgb(255, 255, 255); font-size: 13px; text=
# -decoration: none; font-weight: bold;" target=3D"_blank">Mua ngay &gt;&gt;<=
# /a></td></tr></tbody></table></div></div></td></tr></tbody></table></td></t=
# r>

#                                                     </tbody>

#                                                 </table>

#                                             </td>

#                                             <td valign=3D"top" align=3D"lef=
# t" width=3D"33%" style=3D"padding: 0px; margin: 0px;" class=3D"responsive-c=
# ell">

#                                                 <table cellpadding=3D"0" ce=
# llspacing=3D"0" border=3D"0" width=3D"100%">

#                                                     <tbody>

#                                                         <tr><td align=3D"ce=
# nter" valign=3D"top" style=3D"margin: 0px; padding: 0px;" class=3D"responsi=
# ve-cell"><table cellpadding=3D"0" cellspacing=3D"0" align=3D"center" data-e=
# ditable=3D"image" data-mobile-stretch=3D"1" width=3D"100%"><tbody><tr><td v=
# align=3D"top" align=3D"center" style=3D"display: inline-block; padding: 10p=
# x 0px; margin: 0px;" class=3D"tdBlock responsive-cell"><a href=3D"https://i=
# nmail.inone.useinsider.com/click.html?x=3Da62e&lc=3D81tQ&mc=3Du&s=3DksNEG&u=
# =3DFt&z=3DcuGE9mE&" target=3D"_blank"><img src=3D"https://multimedia.inmail=
# .inone.useinsider.com/insider-BU/photos/323376f2-7232-48bb-b02a-6e380da5961=
# 0.jpg?img1593081522304" width=3D"203" data-src=3D"https://multimedia.inmail=
# .inone.useinsider.com/insider-BU/photos/323376f2-7232-48bb-b02a-6e380da5961=
# 0.jpg|203|203|203|203|0|0|1" height=3D"203" data-origsrc=3D"https://multime=
# dia.inmail.inone.useinsider.com/insider-BU/photos/8c787470-1618-4191-a157-6=
# 71dcb57e7d9.jpg" class=3D"mobile-image-stretch-enabled" style=3D"border-wid=
# th: 0px; border-style: none; border-color: transparent; font-size: 12px; di=
# splay: block;"></a></td></tr></tbody></table></td></tr><tr><td align=3D"cen=
# ter" valign=3D"top" style=3D"margin: 0px; padding: 0px;" class=3D"responsiv=
# e-cell"><table width=3D"100%" border=3D"0" cellpadding=3D"0" cellspacing=3D=
# "0" align=3D"center" data-editable=3D"text" class=3D"text-block"><tbody><tr=
# ><td align=3D"left" valign=3D"top" class=3D"lh-3" style=3D"padding: 10px; f=
# ont-size: 16px; font-family: 'Times New Roman', Times, serif; line-height: =
# 1.35;"><span style=3D"font-family: Arial,'Helvetica Neue', Helvetica, sans-=
# serif; font-size: 17px; font-weight: 700;">Joy 3 4GB</span><br><div class=
# =3D"responsive-cell" style=3D"padding: 0px;"><div><font style=3D"font-size:=
#  17px;"><span style=3D"font-family: Arial,'Helvetica Neue', Helvetica, sans=
# -serif; font-weight: bold; background-color: transparent;"><br></span></fon=
# t></div><div><font style=3D"font-size: 12px;" size=3D"12"><span style=3D"fo=
# nt-family: Arial,'Helvetica Neue', Helvetica, sans-serif; background-color:=
#  transparent; text-decoration: line-through;">3.290.000=C4=91</span></font>=
# </div><div><span style=3D"background-color: transparent; font-family: Arial=
# ,'Helvetica Neue', Helvetica, sans-serif; font-weight: bold; color: rgb(255=
# , 0, 0);"><font style=3D"font-size: 23px;" size=3D"23">3.090.000</font></sp=
# an></div><div data-box=3D"button" style=3D"width: 100%; margin-top: 0px; ma=
# rgin-bottom: 0px; text-align: left;"><table border=3D"0" cellpadding=3D"0" =
# cellspacing=3D"0" align=3D"left" data-editable=3D"button" style=3D"margin: =
# 0px auto 0px 0px;"><tbody><tr><td valign=3D"top" align=3D"center" class=3D"=
# tdBlock" style=3D"display: inline-block; padding: 3px 10px 3px 5px; margin:=
#  0px; background-color: rgb(255, 0, 0); border-radius: 1px;"><a href=3D"htt=
# ps://inmail.inone.useinsider.com/click.html?x=3Da62e&lc=3D81tQ&mc=3Du&s=3Dk=
# sNEG&u=3DFt&z=3DcuXq2XQ&" style=3D"font-family: Arial,'Helvetica Neue', Hel=
# vetica, sans-serif; color: rgb(255, 255, 255); font-size: 13px; text-decora=
# tion: none; font-weight: bold;" target=3D"_blank">Mua ngay &gt;&gt;</a></td=
# ></tr></tbody></table></div></div></td></tr></tbody></table></td></tr>

#                                                        =20

#                                                     </tbody>

#                                                 </table>

#                                             </td>

#                                             <td valign=3D"top" align=3D"lef=
# t" width=3D"33%" style=3D"padding: 0px; margin: 0px;" class=3D"responsive-c=
# ell">

#                                                 <table cellpadding=3D"0" ce=
# llspacing=3D"0" border=3D"0" width=3D"100%">

#                                                     <tbody>

#                                                         <tr><td align=3D"ce=
# nter" valign=3D"top" style=3D"margin: 0px; padding: 0px;" class=3D"responsi=
# ve-cell"><table cellpadding=3D"0" cellspacing=3D"0" align=3D"center" data-e=
# ditable=3D"image" data-mobile-stretch=3D"1" width=3D"100%"><tbody><tr><td v=
# align=3D"top" align=3D"center" style=3D"display: inline-block; padding: 10p=
# x 0px; margin: 0px;" class=3D"tdBlock responsive-cell"><a href=3D"https://i=
# nmail.inone.useinsider.com/click.html?x=3Da62e&lc=3D81t2&mc=3Du&s=3DksNEG&u=
# =3DFt&z=3DczOfSmE&" target=3D"_blank"><img src=3D"https://multimedia.inmail=
# .inone.useinsider.com/insider-BU/photos/35cf32e9-90f5-4317-8a71-2de64f662a8=
# a.jpg?img1593081522304" width=3D"203" data-src=3D"https://multimedia.inmail=
# .inone.useinsider.com/insider-BU/photos/35cf32e9-90f5-4317-8a71-2de64f662a8=
# a.jpg|203|203|203|203|0|0|1" height=3D"203" data-origsrc=3D"https://multime=
# dia.inmail.inone.useinsider.com/insider-BU/photos/9eec90a6-f4be-4076-ab07-8=
# e0e06adeb92.jpg" class=3D"mobile-image-stretch-enabled" style=3D"border-wid=
# th: 0px; border-style: none; border-color: transparent; font-size: 12px; di=
# splay: block;"></a></td></tr></tbody></table></td></tr><tr><td align=3D"cen=
# ter" valign=3D"top" style=3D"margin: 0px; padding: 0px;" class=3D"responsiv=
# e-cell"><table width=3D"100%" border=3D"0" cellpadding=3D"0" cellspacing=3D=
# "0" align=3D"center" data-editable=3D"text" class=3D"text-block"><tbody><tr=
# ><td align=3D"left" valign=3D"top" class=3D"lh-3" style=3D"padding: 10px; f=
# ont-size: 16px; font-family: 'Times New Roman', Times, serif; line-height: =
# 1.35;"><span style=3D"font-family: Arial,'Helvetica Neue', Helvetica, sans-=
# serif; font-size: 17px; font-weight: 700;">Bee</span><br><div class=3D"resp=
# onsive-cell" style=3D"padding: 0px;"><div><font style=3D"font-size: 17px;">=
# <span style=3D"font-family: Arial,'Helvetica Neue', Helvetica, sans-serif; =
# font-weight: bold; background-color: transparent;"><br></span></font></div>=
# <div><font style=3D"font-size: 12px;" size=3D"12"><span style=3D"font-famil=
# y: Arial,'Helvetica Neue', Helvetica, sans-serif; background-color: transpa=
# rent;">Gi=C3=A1 ch=E1=BB=89</span></font></div><div><span style=3D"backgrou=
# nd-color: transparent; font-family: Arial,'Helvetica Neue', Helvetica, sans=
# -serif; font-weight: bold; color: rgb(255, 0, 0);"><font style=3D"font-size=
# : 23px;" size=3D"23">990.000</font></span></div><div data-box=3D"button" st=
# yle=3D"width: 100%; margin-top: 0px; margin-bottom: 0px; text-align: left;"=
# ><table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" align=3D"left" dat=
# a-editable=3D"button" style=3D"margin: 0px auto 0px 0px;"><tbody><tr><td va=
# lign=3D"top" align=3D"center" class=3D"tdBlock" style=3D"display: inline-bl=
# ock; padding: 3px 10px 3px 5px; margin: 0px; background-color: rgb(255, 0, =
# 0); border-radius: 1px;"><a href=3D"https://inmail.inone.useinsider.com/cli=
# ck.html?x=3Da62e&lc=3D81t2&mc=3Du&s=3DksNEG&u=3DFt&z=3DccFAowc&" style=3D"f=
# ont-family: Arial,'Helvetica Neue', Helvetica, sans-serif; color: rgb(255, =
# 255, 255); font-size: 13px; text-decoration: none; font-weight: bold;" targ=
# et=3D"_blank">Mua ngay &gt;&gt;</a></td></tr></tbody></table></div></div></=
# td></tr></tbody></table></td></tr>

#                                                        =20

#                                                     </tbody>

#                                                 </table>

#                                             </td>

#                                         </tr>

#                                     </tbody>

#                                 </table>

#                             </td>

#                         </tr>

#                        =20

#                        =20

#                        =20

#                        =20

#                         <tr><td align=3D"center" valign=3D"top" style=3D"ma=
# rgin: 0px; padding: 0px;" class=3D"responsive-cell"><table width=3D"100%" b=
# order=3D"0" cellpadding=3D"0" cellspacing=3D"0" align=3D"center" data-edita=
# ble=3D"text" class=3D"text-block">

#                                     <tbody>

#                                         <tr>

#                                             <td align=3D"left" valign=3D"to=
# p" class=3D"lh-1" style=3D"padding: 10px; font-size: 16px; font-family: 'Ti=
# mes New Roman', Times, serif; line-height: 1.15; background-color: rgb(128,=
#  128, 128);">

#                                                 <div style=3D"text-align: c=
# enter;"><span style=3D"color: rgb(255, 255, 255); font-family: Arial, Helve=
# tica, sans-serif; font-weight: 700;"><font size=3D"20" style=3D"font-size: =
# 20px;">Xiaomi Ch=C3=ADnh H=C3=A3ng - L=E1=BB=B1a Ch=E1=BB=8Dn =C4=90=C3=A1n=
# g C=C3=A2n Nh=E1=BA=AFc</font></span></div>

#                                             </td>

#                                         </tr>

#                                     </tbody>

#                                 </table></td></tr><tr><td align=3D"center" =
# valign=3D"top" style=3D"margin: 0px; padding: 0px;" class=3D"responsive-cel=
# l"><table cellpadding=3D"0" cellspacing=3D"0" border=3D"0" width=3D"100%"><=
# tbody><tr><td valign=3D"top" align=3D"left" width=3D"33%" style=3D"padding:=
#  0px; margin: 0px;" class=3D"responsive-cell"><table cellpadding=3D"0" cell=
# spacing=3D"0" border=3D"0" width=3D"100%"><tbody><tr><td style=3D"margin: 0=
# px; padding: 0px;" align=3D"center" valign=3D"top" class=3D"responsive-cell=
# "><table cellpadding=3D"0" cellspacing=3D"0" align=3D"center" data-editable=
# =3D"image" data-mobile-stretch=3D"1" width=3D"100%"><tbody><tr><td valign=
# =3D"top" align=3D"center" style=3D"display: inline-block; padding: 10px 0px=
# ; margin: 0px;" class=3D"tdBlock responsive-cell"><a href=3D"https://inmail=
# .inone.useinsider.com/click.html?x=3Da62e&lc=3D81tZ&mc=3Du&s=3DksNEG&u=3DFt=
# &z=3Dc8RJXe1&" target=3D"_blank"><img src=3D"https://multimedia.inmail.inon=
# e.useinsider.com/insider-BU/photos/e63c0d56-f85d-4cca-8a59-46c1fe689757.jpg=
# ?img1593081522304" width=3D"204" data-src=3D"https://multimedia.inmail.inon=
# e.useinsider.com/insider-BU/photos/e63c0d56-f85d-4cca-8a59-46c1fe689757.jpg=
# |204|204|204|204|0|0|1" height=3D"204" data-origsrc=3D"https://multimedia.i=
# nmail.inone.useinsider.com/insider-BU/photos/1549216d-9bdd-4e1f-80bf-95b231=
# 7b176b.jpg" class=3D"mobile-image-stretch-enabled" style=3D"border-width: 0=
# px; border-style: none; border-color: transparent; font-size: 12px; display=
# : block;"></a></td></tr></tbody></table></td></tr><tr><td align=3D"center" =
# valign=3D"top" style=3D"margin: 0px; padding: 0px;" class=3D"responsive-cel=
# l"><table width=3D"100%" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" a=
# lign=3D"center" data-editable=3D"text" class=3D"text-block">

#                                                                     <tbody>

#                                                                         <tr=
# >

#                                                                            =
#  <td align=3D"left" valign=3D"top" class=3D"lh-3" style=3D"padding: 10px; f=
# ont-size: 16px; font-family: 'Times New Roman', Times, serif; line-height: =
# 1.35;"><font style=3D"font-size: 17px;"><span style=3D"font-family: Arial,'=
# Helvetica Neue', Helvetica, sans-serif; font-weight: bold;">Redmi Note 9</s=
# pan></font><div>

#                                                                            =
#      <div class=3D"responsive-cell" style=3D"padding: 0px;">

#                                                                            =
#          <div><span style=3D"background-color: transparent; font-family: Ar=
# ial,'Helvetica Neue', Helvetica, sans-serif; text-decoration: line-through;=
#  font-size: 12px;"><br></span></div><div><span style=3D"background-color: t=
# ransparent; font-family: Arial,'Helvetica Neue', Helvetica, sans-serif; tex=
# t-decoration: line-through; font-size: 12px;">4.990.000=C4=91</span><br></d=
# iv>

#                                                                            =
#          <div>

#                                                                            =
#              <span style=3D"background-color: transparent; font-family: Ari=
# al,'Helvetica Neue', Helvetica, sans-serif; font-weight: bold; color: rgb(2=
# 55, 0, 0);">

#                                                                            =
#                  <font style=3D"font-size: 23px;" size=3D"23">4.600.000</fo=
# nt>

#                                                                            =
#              </span>

#                                                                            =
#          </div>

#                                                                            =
#          <div data-box=3D"button" style=3D"width: 100%; margin-top: 0px; ma=
# rgin-bottom: 0px; text-align: left;"><table border=3D"0" cellpadding=3D"0" =
# cellspacing=3D"0" align=3D"left" data-editable=3D"button" style=3D"margin: =
# 0px auto 0px 0px;">

#                                                                            =
#                  <tbody>

#                                                                            =
#                      <tr>

#                                                                            =
#                          <td valign=3D"top" align=3D"center" class=3D"tdBlo=
# ck" style=3D"display: inline-block; padding: 3px 10px 3px 5px; margin: 0px;=
#  background-color: rgb(255, 0, 0); border-radius: 1px;"><a href=3D"https://=
# inmail.inone.useinsider.com/click.html?x=3Da62e&lc=3D81tZ&mc=3Du&s=3DksNEG&=
# u=3DFt&z=3DcoIsPaO&" style=3D"

#                                                                            =
#                                      font-family: Arial,'Helvetica Neue', H=
# elvetica, sans-serif;

#                                                                            =
#                                      color: rgb(255, 255, 255);

#                                                                            =
#                                      font-size: 13px;

#                                                                            =
#                                      text-decoration: none;

#                                                                            =
#                                      font-weight: bold;

#                                                                            =
#                                  " target=3D"_blank">

#                                                                            =
#                                  Mua ngay &gt;&gt;

#                                                                            =
#                              </a></td>

#                                                                            =
#                      </tr>

#                                                                            =
#                  </tbody>

#                                                                            =
#              </table></div>

#                                                                            =
#      </div>

#                                                                            =
#  </div></td>

#                                                                         </t=
# r>

#                                                                     </tbody=
# >

#                                                                 </table></t=
# d></tr></tbody></table></td><td valign=3D"top" align=3D"left" width=3D"33%"=
#  style=3D"padding: 0px; margin: 0px;" class=3D"responsive-cell"><table cell=
# padding=3D"0" cellspacing=3D"0" border=3D"0" width=3D"100%"><tbody><tr><td =
# style=3D"margin: 0px; padding: 0px;" align=3D"center" valign=3D"top" class=
# =3D"responsive-cell"><table cellpadding=3D"0" cellspacing=3D"0" align=3D"ce=
# nter" data-editable=3D"image" data-mobile-stretch=3D"1" width=3D"100%"><tbo=
# dy><tr><td valign=3D"top" align=3D"center" style=3D"display: inline-block; =
# padding: 10px 0px; margin: 0px;" class=3D"tdBlock responsive-cell"><a href=
# =3D"https://inmail.inone.useinsider.com/click.html?x=3Da62e&lc=3D81te&mc=3D=
# u&s=3DksNEG&u=3DFt&z=3DcpSV20F&" target=3D"_blank"><img src=3D"https://mult=
# imedia.inmail.inone.useinsider.com/insider-BU/photos/76ce2e5c-f765-4775-98a=
# e-27fb8a06f1b3.jpg?img1593081522304" width=3D"204" data-src=3D"https://mult=
# imedia.inmail.inone.useinsider.com/insider-BU/photos/76ce2e5c-f765-4775-98a=
# e-27fb8a06f1b3.jpg|204|204|204|204|0|0|1" height=3D"204" data-origsrc=3D"ht=
# tps://multimedia.inmail.inone.useinsider.com/insider-BU/photos/b129519e-bcd=
# 1-491f-a7bc-892c0e30a599.jpg" class=3D"mobile-image-stretch-enabled" style=
# =3D"border-width: 0px; border-style: none; border-color: transparent; font-=
# size: 12px; display: block;"></a></td></tr></tbody></table></td></tr><tr><t=
# d align=3D"center" valign=3D"top" style=3D"margin: 0px; padding: 0px;" clas=
# s=3D"responsive-cell"><table width=3D"100%" border=3D"0" cellpadding=3D"0" =
# cellspacing=3D"0" align=3D"center" data-editable=3D"text" class=3D"text-blo=
# ck">

#                                                                     <tbody>

#                                                                         <tr=
# >

#                                                                            =
#  <td align=3D"left" valign=3D"top" class=3D"lh-3" style=3D"padding: 10px; f=
# ont-size: 16px; font-family: 'Times New Roman', Times, serif; line-height: =
# 1.35;"><font style=3D"font-size: 17px;"><span style=3D"font-family: Arial,'=
# Helvetica Neue', Helvetica, sans-serif; font-weight: bold;">Redmi Note 9s</=
# span></font><div>

#                                                                            =
#      <div class=3D"responsive-cell" style=3D"padding: 0px;">

#                                                                            =
#          <div><span style=3D"background-color: transparent; font-family: Ar=
# ial,'Helvetica Neue', Helvetica, sans-serif; text-decoration: line-through;=
#  font-size: 12px;"><br></span></div><div><span style=3D"background-color: t=
# ransparent; font-family: Arial,'Helvetica Neue', Helvetica, sans-serif; tex=
# t-decoration: line-through; font-size: 12px;">5.490.000=C4=91</span><br></d=
# iv>

#                                                                            =
#          <div>

#                                                                            =
#              <span style=3D"background-color: transparent; font-family: Ari=
# al,'Helvetica Neue', Helvetica, sans-serif; font-weight: bold; color: rgb(2=
# 55, 0, 0);">

#                                                                            =
#                  <font style=3D"font-size: 23px;" size=3D"23">4.900.000</fo=
# nt>

#                                                                            =
#              </span>

#                                                                            =
#          </div>

#                                                                            =
#          <div data-box=3D"button" style=3D"width: 100%; margin-top: 0px; ma=
# rgin-bottom: 0px; text-align: left;"><table border=3D"0" cellpadding=3D"0" =
# cellspacing=3D"0" align=3D"left" data-editable=3D"button" style=3D"margin: =
# 0px auto 0px 0px;">

#                                                                            =
#                  <tbody>

#                                                                            =
#                      <tr>

#                                                                            =
#                          <td valign=3D"top" align=3D"center" class=3D"tdBlo=
# ck" style=3D"display: inline-block; padding: 3px 10px 3px 5px; margin: 0px;=
#  background-color: rgb(255, 0, 0); border-radius: 1px;"><a href=3D"https://=
# inmail.inone.useinsider.com/click.html?x=3Da62e&lc=3D81te&mc=3Du&s=3DksNEG&=
# u=3DFt&z=3DcQhKmxQ&" style=3D"

#                                                                            =
#                                      font-family: Arial,'Helvetica Neue', H=
# elvetica, sans-serif;

#                                                                            =
#                                      color: rgb(255, 255, 255);

#                                                                            =
#                                      font-size: 13px;

#                                                                            =
#                                      text-decoration: none;

#                                                                            =
#                                      font-weight: bold;

#                                                                            =
#                                  " target=3D"_blank">

#                                                                            =
#                                  Mua ngay &gt;&gt;

#                                                                            =
#                              </a></td>

#                                                                            =
#                      </tr>

#                                                                            =
#                  </tbody>

#                                                                            =
#              </table></div>

#                                                                            =
#      </div>

#                                                                            =
#  </div></td>

#                                                                         </t=
# r>

#                                                                     </tbody=
# >

#                                                                 </table></t=
# d></tr></tbody></table></td><td valign=3D"top" align=3D"left" width=3D"33%"=
#  style=3D"padding: 0px; margin: 0px;" class=3D"responsive-cell"><table cell=
# padding=3D"0" cellspacing=3D"0" border=3D"0" width=3D"100%"><tbody><tr><td =
# style=3D"margin: 0px; padding: 0px;" align=3D"center" valign=3D"top" class=
# =3D"responsive-cell"><table cellpadding=3D"0" cellspacing=3D"0" align=3D"ce=
# nter" data-editable=3D"image" data-mobile-stretch=3D"1" width=3D"100%"><tbo=
# dy><tr><td valign=3D"top" align=3D"center" style=3D"display: inline-block; =
# padding: 10px 0px; margin: 0px;" class=3D"tdBlock responsive-cell"><a href=
# =3D"https://inmail.inone.useinsider.com/click.html?x=3Da62e&lc=3D81tn&mc=3D=
# u&s=3DksNEG&u=3DFt&z=3DcQ4IqJn&" target=3D"_blank"><img src=3D"https://mult=
# imedia.inmail.inone.useinsider.com/insider-BU/photos/5f544018-859c-4871-974=
# 7-0b9805b1e702.jpg?img1593081522304" width=3D"204" data-src=3D"https://mult=
# imedia.inmail.inone.useinsider.com/insider-BU/photos/5f544018-859c-4871-974=
# 7-0b9805b1e702.jpg|204|204|204|204|0|0|1" height=3D"204" data-origsrc=3D"ht=
# tps://multimedia.inmail.inone.useinsider.com/insider-BU/photos/d384188a-9d4=
# b-42af-ad4c-3dbecfe1e368.jpg" class=3D"mobile-image-stretch-enabled" style=
# =3D"border-width: 0px; border-style: none; border-color: transparent; font-=
# size: 12px; display: block;"></a></td></tr></tbody></table></td></tr><tr><t=
# d align=3D"center" valign=3D"top" style=3D"margin: 0px; padding: 0px;" clas=
# s=3D"responsive-cell"><table width=3D"100%" border=3D"0" cellpadding=3D"0" =
# cellspacing=3D"0" align=3D"center" data-editable=3D"text" class=3D"text-blo=
# ck">

#                                                                     <tbody>

#                                                                         <tr=
# >

#                                                                            =
#  <td align=3D"left" valign=3D"top" class=3D"lh-3" style=3D"padding: 10px; f=
# ont-size: 16px; font-family: 'Times New Roman', Times, serif; line-height: =
# 1.35;"><font style=3D"font-size: 17px;"><span style=3D"font-family: Arial,'=
# Helvetica Neue', Helvetica, sans-serif; font-weight: bold;">Redmi Note 8 Pr=
# o</span></font><div>

#                                                                            =
#      <div class=3D"responsive-cell" style=3D"padding: 0px;">

#                                                                            =
#          <div><span style=3D"background-color: transparent; font-family: Ar=
# ial,'Helvetica Neue', Helvetica, sans-serif; text-decoration: line-through;=
#  font-size: 12px;"><br></span></div><div><span style=3D"background-color: t=
# ransparent; font-family: Arial,'Helvetica Neue', Helvetica, sans-serif; tex=
# t-decoration: line-through; font-size: 12px;">5.490.000=C4=91</span><br></d=
# iv>

#                                                                            =
#          <div>

#                                                                            =
#              <span style=3D"background-color: transparent; font-family: Ari=
# al,'Helvetica Neue', Helvetica, sans-serif; font-weight: bold; color: rgb(2=
# 55, 0, 0);">

#                                                                            =
#                  <font style=3D"font-size: 23px;" size=3D"23">5.050.000</fo=
# nt>

#                                                                            =
#              </span>

#                                                                            =
#          </div>

#                                                                            =
#          <div data-box=3D"button" style=3D"width: 100%; margin-top: 0px; ma=
# rgin-bottom: 0px; text-align: left;"><table border=3D"0" cellpadding=3D"0" =
# cellspacing=3D"0" align=3D"left" data-editable=3D"button" style=3D"margin: =
# 0px auto 0px 0px;">

#                                                                            =
#                  <tbody>

#                                                                            =
#                      <tr>

#                                                                            =
#                          <td valign=3D"top" align=3D"center" class=3D"tdBlo=
# ck" style=3D"display: inline-block; padding: 3px 10px 3px 5px; margin: 0px;=
#  background-color: rgb(255, 0, 0); border-radius: 1px;"><a href=3D"https://=
# inmail.inone.useinsider.com/click.html?x=3Da62e&lc=3D81tn&mc=3Du&s=3DksNEG&=
# u=3DFt&z=3DcmsRmBn&" style=3D"

#                                                                            =
#                                      font-family: Arial,'Helvetica Neue', H=
# elvetica, sans-serif;

#                                                                            =
#                                      color: rgb(255, 255, 255);

#                                                                            =
#                                      font-size: 13px;

#                                                                            =
#                                      text-decoration: none;

#                                                                            =
#                                      font-weight: bold;

#                                                                            =
#                                  " target=3D"_blank">

#                                                                            =
#                                  Mua ngay &gt;&gt;

#                                                                            =
#                              </a></td>

#                                                                            =
#                      </tr>

#                                                                            =
#                  </tbody>

#                                                                            =
#              </table></div>

#                                                                            =
#      </div>

#                                                                            =
#  </div></td>

#                                                                         </t=
# r>

#                                                                     </tbody=
# >

#                                                                 </table></t=
# d></tr></tbody></table></td></tr></tbody></table></td></tr><tr><td align=3D=
# "center" valign=3D"top" style=3D"padding: 10px 0px;" class=3D"responsive-ce=
# ll"><div data-box=3D"button" style=3D"width: 100%; margin-top: 0px; margin-=
# bottom: 0px; text-align: center;"><table border=3D"0" cellpadding=3D"0" cel=
# lspacing=3D"0" align=3D"center" data-editable=3D"button" style=3D"margin: 0=
# px auto;">

#                                         <tbody>

#                                             <tr>

#                                                 <td valign=3D"top" align=3D=
# "center" class=3D"tdBlock" style=3D"display: inline-block; padding: 13px 25=
# px; margin: 0px; background-color: rgb(251, 18, 18); border-radius: 24px; w=
# idth: 521px;"><a href=3D"https://inmail.inone.useinsider.com/click.html?x=
# =3Da62e&lc=3D81td&mc=3Du&s=3DksNEG&u=3DFt&z=3DcqMV2PW&" style=3D"font-famil=
# y: Arial,'Helvetica Neue', Helvetica, sans-serif; color: rgb(255, 255, 255)=
# ; font-size: 18px; text-decoration: none; font-weight: bold;" target=3D"_bl=
# ank">Xem th=C3=AAm =C4=91i=E1=BB=87n tho=E1=BA=A1i kh=C3=A1c &gt;&gt;

#                                                     </a></td>

#                                             </tr>

#                                         </tbody>

#                                     </table></div></td></tr><tr>

#                             <td align=3D"center" valign=3D"top" style=3D"ma=
# rgin: 0px; padding: 0px;" class=3D"responsive-cell">

#                                 <table border=3D"0" cellpadding=3D"0" cells=
# pacing=3D"0" align=3D"center" width=3D"100%" data-editable=3D"line" style=
# =3D"">

#                                     <tbody>

#                                         <tr>

#                                             <td valign=3D"top" align=3D"cen=
# ter" style=3D"padding: 10px 0px; margin: 0px;"><div style=3D"height: 1px; l=
# ine-height: 1px; border-top: 1px solid rgb(251, 18, 18);">

#                                                     <img src=3D"data:image/=
# gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=3D=3D=
# " alt=3D"" width=3D"1" height=3D"1" style=3D"display: block;" createnew=3D"=
# true">

#                                                 </div></td>

#                                         </tr>

#                                     </tbody>

#                                 </table>

#                             </td>

#                         </tr>

#                        =20

#                        =20

#                        =20

#                         <tr><td align=3D"center" valign=3D"top" style=3D"ma=
# rgin: 0px; padding: 0px;" class=3D"responsive-cell"><table width=3D"100%" b=
# order=3D"0" cellpadding=3D"0" cellspacing=3D"0" align=3D"center" data-edita=
# ble=3D"text" class=3D"text-block">

#                                     <tbody>

#                                         <tr>

#                                             <td align=3D"left" valign=3D"to=
# p" class=3D"lh-1" style=3D"padding: 10px; font-size: 16px; font-family: 'Ti=
# mes New Roman', Times, serif; line-height: 1.15; background-color: rgb(128,=
#  128, 128);">

#                                                 <div style=3D"text-align: c=
# enter;">

#                                                     <span style=3D"color: r=
# gb(255, 255, 255); font-family: Arial, Helvetica, sans-serif; font-weight: =
# 700;">

#                                                         <font size=3D"20" s=
# tyle=3D"font-size: 20px;">C=C3=B3 th=E1=BB=83&nbsp;b=E1=BA=A1n c=C5=A9ng th=
# =C3=ADch</font>

#                                                     </span>

#                                                 </div>

#                                             </td>

#                                         </tr>

#                                     </tbody>

#                                 </table></td></tr><tr>

#                             <td align=3D"center" valign=3D"top" style=3D"ma=
# rgin: 0px; padding: 0px;" class=3D"responsive-cell">

# <table style=3D"background-color:white" width=3D"100%">

#     <tbody>

#         <tr>

#             <td style=3D"text-align:center;font-family:Arial;font-weight:no=
# rmal;font-size:0px;color:#000000;text-decoration:none;font-style:normal;wid=
# th: 600px;padding-bottom: 10px;">Recommended Products </td>

#         </tr>

#     </tbody>

# </table>

# <table width=3D"100%">

#     <tbody>

#     <tr>

#     <td>

#         <a style=3D"text-decoration: none;" href=3D"https://inmail.inone.us=
# einsider.com/click.html?x=3Da62e&lc=3D81tB&mc=3Du&s=3DksNEG&u=3DFt&z=3DccPn=
# 2L0&">

#             <img createnew=3D"true" src=3D"https://mail-recommendation.api.=
# useinsider.com/img?email=3Dnguyen.dphux@gmail.com&amp;language=3Dvi_VN&amp;=
# currency=3DVND&amp;rtype=3Duser-based&amp;pid=3D10002648&amp;cid=3D52&amp;p=
# lace=3D1&amp;slots=3D6&amp;settings=3DeyJub2NhY2hlIjoxLCJ0aXRsZSI6eyJvbiI6M=
# SwiZiI6IkFyaWFsIiwicyI6MTIsImMiOiIjMDAwMDAwIiwic3QiOiJSZWd1bGFyIiwiYSI6ImNl=
# bnRlciIsImQiOiIifSwicHJpY2UiOnsib24iOjEsImYiOiJBcmlhbCIsInMiOjEwLCJjIjoiIzA=
# wMDAwMCIsInN0IjoiUmVndWxhciIsImEiOiJjZW50ZXIiLCJkIjoi4oCUIn0sImRpc2NvdW50Ij=
# p7Im9uIjoxLCJmIjoiQXJpYWwiLCJzIjoxMiwiYyI6IiNmZjAwMDAiLCJzdCI6IkJvbGQiLCJhI=
# joiY2VudGVyIiwiZCI6IiJ9LCJjdXJyZW5jeSI6eyJzIjoixJEiLCJzbCI6ImFmdGVyIiwidHMi=
# OiIsIiwiZHMiOiJubyJ9LCJ0aXRsZVN0eWxpbmciOnsiZiI6IkFyaWFsIiwicyI6MTgsImMiOiI=
# jMDAwMDAwIiwic3QiOiJSZWd1bGFyIiwiYSI6ImNlbnRlciIsImQiOiJub25lIn19&amp;filte=
# rs[]=3D[category][!~][%C4%90i%E1%BB%87n%20tho%E1%BA%A1i]&amp;filters[]=3D[c=
# ategory][!~][H%C3%A0ng%20c%C5%A9]&amp;filters[]=3D[category][!~][%C4%90%E1%=
# BB%93ng%20h%E1%BB%93]&amp;filters[]=3D[category][!~][Tablet]&amp;utm_source=
# =3Dinsider&amp;utm_medium=3Demail_recommendation&amp;utm_campaign=3D2020062=
# 2_Apple">

#         </a>

#     </td>

# <td>

#         <a style=3D"text-decoration: none;" href=3D"https://inmail.inone.us=
# einsider.com/click.html?x=3Da62e&lc=3D81tH&mc=3Du&s=3DksNEG&u=3DFt&z=3Dcky4=
# SKM&">

#             <img createnew=3D"true" src=3D"https://mail-recommendation.api.=
# useinsider.com/img?email=3Dnguyen.dphux@gmail.com&amp;language=3Dvi_VN&amp;=
# currency=3DVND&amp;rtype=3Duser-based&amp;pid=3D10002648&amp;cid=3D52&amp;p=
# lace=3D2&amp;slots=3D6&amp;settings=3DeyJub2NhY2hlIjoxLCJ0aXRsZSI6eyJvbiI6M=
# SwiZiI6IkFyaWFsIiwicyI6MTIsImMiOiIjMDAwMDAwIiwic3QiOiJSZWd1bGFyIiwiYSI6ImNl=
# bnRlciIsImQiOiIifSwicHJpY2UiOnsib24iOjEsImYiOiJBcmlhbCIsInMiOjEwLCJjIjoiIzA=
# wMDAwMCIsInN0IjoiUmVndWxhciIsImEiOiJjZW50ZXIiLCJkIjoi4oCUIn0sImRpc2NvdW50Ij=
# p7Im9uIjoxLCJmIjoiQXJpYWwiLCJzIjoxMiwiYyI6IiNmZjAwMDAiLCJzdCI6IkJvbGQiLCJhI=
# joiY2VudGVyIiwiZCI6IiJ9LCJjdXJyZW5jeSI6eyJzIjoixJEiLCJzbCI6ImFmdGVyIiwidHMi=
# OiIsIiwiZHMiOiJubyJ9LCJ0aXRsZVN0eWxpbmciOnsiZiI6IkFyaWFsIiwicyI6MTgsImMiOiI=
# jMDAwMDAwIiwic3QiOiJSZWd1bGFyIiwiYSI6ImNlbnRlciIsImQiOiJub25lIn19&amp;filte=
# rs[]=3D[category][!~][%C4%90i%E1%BB%87n%20tho%E1%BA%A1i]&amp;filters[]=3D[c=
# ategory][!~][H%C3%A0ng%20c%C5%A9]&amp;filters[]=3D[category][!~][%C4%90%E1%=
# BB%93ng%20h%E1%BB%93]&amp;filters[]=3D[category][!~][Tablet]&amp;utm_source=
# =3Dinsider&amp;utm_medium=3Demail_recommendation&amp;utm_campaign=3D2020062=
# 2_Apple">

#         </a>

#     </td>

# <td>

#         <a style=3D"text-decoration: none;" href=3D"https://inmail.inone.us=
# einsider.com/click.html?x=3Da62e&lc=3D81tr&mc=3Du&s=3DksNEG&u=3DFt&z=3DczXO=
# Vb&">

#             <img createnew=3D"true" src=3D"https://mail-recommendation.api.=
# useinsider.com/img?email=3Dnguyen.dphux@gmail.com&amp;language=3Dvi_VN&amp;=
# currency=3DVND&amp;rtype=3Duser-based&amp;pid=3D10002648&amp;cid=3D52&amp;p=
# lace=3D3&amp;slots=3D6&amp;settings=3DeyJub2NhY2hlIjoxLCJ0aXRsZSI6eyJvbiI6M=
# SwiZiI6IkFyaWFsIiwicyI6MTIsImMiOiIjMDAwMDAwIiwic3QiOiJSZWd1bGFyIiwiYSI6ImNl=
# bnRlciIsImQiOiIifSwicHJpY2UiOnsib24iOjEsImYiOiJBcmlhbCIsInMiOjEwLCJjIjoiIzA=
# wMDAwMCIsInN0IjoiUmVndWxhciIsImEiOiJjZW50ZXIiLCJkIjoi4oCUIn0sImRpc2NvdW50Ij=
# p7Im9uIjoxLCJmIjoiQXJpYWwiLCJzIjoxMiwiYyI6IiNmZjAwMDAiLCJzdCI6IkJvbGQiLCJhI=
# joiY2VudGVyIiwiZCI6IiJ9LCJjdXJyZW5jeSI6eyJzIjoixJEiLCJzbCI6ImFmdGVyIiwidHMi=
# OiIsIiwiZHMiOiJubyJ9LCJ0aXRsZVN0eWxpbmciOnsiZiI6IkFyaWFsIiwicyI6MTgsImMiOiI=
# jMDAwMDAwIiwic3QiOiJSZWd1bGFyIiwiYSI6ImNlbnRlciIsImQiOiJub25lIn19&amp;filte=
# rs[]=3D[category][!~][%C4%90i%E1%BB%87n%20tho%E1%BA%A1i]&amp;filters[]=3D[c=
# ategory][!~][H%C3%A0ng%20c%C5%A9]&amp;filters[]=3D[category][!~][%C4%90%E1%=
# BB%93ng%20h%E1%BB%93]&amp;filters[]=3D[category][!~][Tablet]&amp;utm_source=
# =3Dinsider&amp;utm_medium=3Demail_recommendation&amp;utm_campaign=3D2020062=
# 2_Apple">

#         </a>

#     </td>

#     </tr>

# <tr>

#     <td>

#         <a style=3D"text-decoration: none;" href=3D"https://inmail.inone.us=
# einsider.com/click.html?x=3Da62e&lc=3D81tA&mc=3Du&s=3DksNEG&u=3DFt&z=3DcuWN=
# 9WF&">

#             <img createnew=3D"true" src=3D"https://mail-recommendation.api.=
# useinsider.com/img?email=3Dnguyen.dphux@gmail.com&amp;language=3Dvi_VN&amp;=
# currency=3DVND&amp;rtype=3Duser-based&amp;pid=3D10002648&amp;cid=3D52&amp;p=
# lace=3D4&amp;slots=3D6&amp;settings=3DeyJub2NhY2hlIjoxLCJ0aXRsZSI6eyJvbiI6M=
# SwiZiI6IkFyaWFsIiwicyI6MTIsImMiOiIjMDAwMDAwIiwic3QiOiJSZWd1bGFyIiwiYSI6ImNl=
# bnRlciIsImQiOiIifSwicHJpY2UiOnsib24iOjEsImYiOiJBcmlhbCIsInMiOjEwLCJjIjoiIzA=
# wMDAwMCIsInN0IjoiUmVndWxhciIsImEiOiJjZW50ZXIiLCJkIjoi4oCUIn0sImRpc2NvdW50Ij=
# p7Im9uIjoxLCJmIjoiQXJpYWwiLCJzIjoxMiwiYyI6IiNmZjAwMDAiLCJzdCI6IkJvbGQiLCJhI=
# joiY2VudGVyIiwiZCI6IiJ9LCJjdXJyZW5jeSI6eyJzIjoixJEiLCJzbCI6ImFmdGVyIiwidHMi=
# OiIsIiwiZHMiOiJubyJ9LCJ0aXRsZVN0eWxpbmciOnsiZiI6IkFyaWFsIiwicyI6MTgsImMiOiI=
# jMDAwMDAwIiwic3QiOiJSZWd1bGFyIiwiYSI6ImNlbnRlciIsImQiOiJub25lIn19&amp;filte=
# rs[]=3D[category][!~][%C4%90i%E1%BB%87n%20tho%E1%BA%A1i]&amp;filters[]=3D[c=
# ategory][!~][H%C3%A0ng%20c%C5%A9]&amp;filters[]=3D[category][!~][%C4%90%E1%=
# BB%93ng%20h%E1%BB%93]&amp;filters[]=3D[category][!~][Tablet]&amp;utm_source=
# =3Dinsider&amp;utm_medium=3Demail_recommendation&amp;utm_campaign=3D2020062=
# 2_Apple">

#         </a>

#     </td>

# <td>

#         <a style=3D"text-decoration: none;" href=3D"https://inmail.inone.us=
# einsider.com/click.html?x=3Da62e&lc=3D81tE&mc=3Du&s=3DksNEG&u=3DFt&z=3Dc8IT=
# mfM&">

#             <img createnew=3D"true" src=3D"https://mail-recommendation.api.=
# useinsider.com/img?email=3Dnguyen.dphux@gmail.com&amp;language=3Dvi_VN&amp;=
# currency=3DVND&amp;rtype=3Duser-based&amp;pid=3D10002648&amp;cid=3D52&amp;p=
# lace=3D5&amp;slots=3D6&amp;settings=3DeyJub2NhY2hlIjoxLCJ0aXRsZSI6eyJvbiI6M=
# SwiZiI6IkFyaWFsIiwicyI6MTIsImMiOiIjMDAwMDAwIiwic3QiOiJSZWd1bGFyIiwiYSI6ImNl=
# bnRlciIsImQiOiIifSwicHJpY2UiOnsib24iOjEsImYiOiJBcmlhbCIsInMiOjEwLCJjIjoiIzA=
# wMDAwMCIsInN0IjoiUmVndWxhciIsImEiOiJjZW50ZXIiLCJkIjoi4oCUIn0sImRpc2NvdW50Ij=
# p7Im9uIjoxLCJmIjoiQXJpYWwiLCJzIjoxMiwiYyI6IiNmZjAwMDAiLCJzdCI6IkJvbGQiLCJhI=
# joiY2VudGVyIiwiZCI6IiJ9LCJjdXJyZW5jeSI6eyJzIjoixJEiLCJzbCI6ImFmdGVyIiwidHMi=
# OiIsIiwiZHMiOiJubyJ9LCJ0aXRsZVN0eWxpbmciOnsiZiI6IkFyaWFsIiwicyI6MTgsImMiOiI=
# jMDAwMDAwIiwic3QiOiJSZWd1bGFyIiwiYSI6ImNlbnRlciIsImQiOiJub25lIn19&amp;filte=
# rs[]=3D[category][!~][%C4%90i%E1%BB%87n%20tho%E1%BA%A1i]&amp;filters[]=3D[c=
# ategory][!~][H%C3%A0ng%20c%C5%A9]&amp;filters[]=3D[category][!~][%C4%90%E1%=
# BB%93ng%20h%E1%BB%93]&amp;filters[]=3D[category][!~][Tablet]&amp;utm_source=
# =3Dinsider&amp;utm_medium=3Demail_recommendation&amp;utm_campaign=3D2020062=
# 2_Apple">

#         </a>

#     </td>

# <td>

#         <a style=3D"text-decoration: none;" href=3D"https://inmail.inone.us=
# einsider.com/click.html?x=3Da62e&lc=3D81tY&mc=3Du&s=3DksNEG&u=3DFt&z=3Dc95u=
# mFA&">

#             <img createnew=3D"true" src=3D"https://mail-recommendation.api.=
# useinsider.com/img?email=3Dnguyen.dphux@gmail.com&amp;language=3Dvi_VN&amp;=
# currency=3DVND&amp;rtype=3Duser-based&amp;pid=3D10002648&amp;cid=3D52&amp;p=
# lace=3D6&amp;slots=3D6&amp;settings=3DeyJub2NhY2hlIjoxLCJ0aXRsZSI6eyJvbiI6M=
# SwiZiI6IkFyaWFsIiwicyI6MTIsImMiOiIjMDAwMDAwIiwic3QiOiJSZWd1bGFyIiwiYSI6ImNl=
# bnRlciIsImQiOiIifSwicHJpY2UiOnsib24iOjEsImYiOiJBcmlhbCIsInMiOjEwLCJjIjoiIzA=
# wMDAwMCIsInN0IjoiUmVndWxhciIsImEiOiJjZW50ZXIiLCJkIjoi4oCUIn0sImRpc2NvdW50Ij=
# p7Im9uIjoxLCJmIjoiQXJpYWwiLCJzIjoxMiwiYyI6IiNmZjAwMDAiLCJzdCI6IkJvbGQiLCJhI=
# joiY2VudGVyIiwiZCI6IiJ9LCJjdXJyZW5jeSI6eyJzIjoixJEiLCJzbCI6ImFmdGVyIiwidHMi=
# OiIsIiwiZHMiOiJubyJ9LCJ0aXRsZVN0eWxpbmciOnsiZiI6IkFyaWFsIiwicyI6MTgsImMiOiI=
# jMDAwMDAwIiwic3QiOiJSZWd1bGFyIiwiYSI6ImNlbnRlciIsImQiOiJub25lIn19&amp;filte=
# rs[]=3D[category][!~][%C4%90i%E1%BB%87n%20tho%E1%BA%A1i]&amp;filters[]=3D[c=
# ategory][!~][H%C3%A0ng%20c%C5%A9]&amp;filters[]=3D[category][!~][%C4%90%E1%=
# BB%93ng%20h%E1%BB%93]&amp;filters[]=3D[category][!~][Tablet]&amp;utm_source=
# =3Dinsider&amp;utm_medium=3Demail_recommendation&amp;utm_campaign=3D2020062=
# 2_Apple">

#         </a>

#     </td>

#     </tr>

#     </tbody>

# </table>

#                             </td>

#                         </tr>

#                         <tr>

#                             <td align=3D"center" valign=3D"top" style=3D"ma=
# rgin: 0px; padding: 0px;" class=3D"responsive-cell">

#                                 <table border=3D"0" cellpadding=3D"0" cells=
# pacing=3D"0" align=3D"center" width=3D"100%" data-editable=3D"line" style=
# =3D"">

#                                     <tbody>

#                                         <tr>

#                                             <td valign=3D"top" align=3D"cen=
# ter" style=3D"padding: 10px 0px; margin: 0px;"><div style=3D"height: 1px; l=
# ine-height: 1px; border-top: 1px solid rgb(251, 18, 18);">

#                                                     <img src=3D"data:image/=
# gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=3D=3D=
# " alt=3D"" width=3D"1" height=3D"1" style=3D"display: block;" createnew=3D"=
# true">

#                                                 </div></td>

#                                         </tr>

#                                     </tbody>

#                                 </table>

#                                =20

#                             </td>

#                         </tr>

#                         <tr>

#                             <td align=3D"center" valign=3D"top" style=3D"ma=
# rgin: 0px; padding: 0px;" class=3D"responsive-cell">

#                                 <table width=3D"100%" border=3D"0" cellpadd=
# ing=3D"0" cellspacing=3D"0" align=3D"center" data-editable=3D"text" class=
# =3D"text-block">

#                                     <tbody>

#                                         <tr>

#                                             <td align=3D"left" valign=3D"to=
# p" class=3D"lh-2" style=3D"padding: 10px; font-size: 25px; font-family: 'Ti=
# mes New Roman', Times, serif; line-height: 1.25;">

#                                                 <div style=3D"text-align: c=
# enter;"><span style=3D"color: rgb(38, 38, 38); font-family: Arial, Helvetic=
# a, sans-serif;">Tham kh=E1=BA=A3o th=C3=AAm c=C3=A1c s=E1=BA=A3n ph=E1=BA=
# =A9m kh=C3=A1c?</span></div>

#                                             </td>

#                                         </tr>

#                                     </tbody>

#                                 </table>

#                             </td>

#                         </tr>

#                         <tr>

#                             <td align=3D"center" valign=3D"top" style=3D"pa=
# dding: 0px 0px 10px;" class=3D"responsive-cell">

#                                 <div data-box=3D"button" style=3D"width: 10=
# 0%; margin-top: 0px; margin-bottom: 0px; text-align: center;"><table border=
# =3D"0" cellpadding=3D"0" cellspacing=3D"0" align=3D"center" data-editable=
# =3D"button" style=3D"margin: 0px auto;">

#                                         <tbody>

#                                             <tr>

#                                                 <td valign=3D"top" align=3D=
# "center" class=3D"tdBlock" style=3D"display: inline-block; padding: 7px 25p=
# x; margin: 0px; background-color: rgb(251, 18, 18); border-radius: 24px; bo=
# rder-top-width: 1px; border-top-color: rgb(251, 18, 18); width: 357px;"><a =
# href=3D"https://inmail.inone.useinsider.com/click.html?x=3Da62e&lc=3D81td&m=
# c=3Du&s=3DksNEG&u=3DFt&z=3DcmthSXG&" style=3D"

#                                                             font-family: Ar=
# ial,'Helvetica Neue', Helvetica, sans-serif;

#                                                             color: rgb(255,=
#  255, 255);

#                                                             font-size: 19px=
# ;

#                                                             text-decoration=
# : none;

#                                                             font-weight: bo=
# ld;

#                                                             background-colo=
# r: transparent;

#                                                             font-style: ita=
# lic;

#                                                         " target=3D"_blank"=
# >

#                                                         T=E1=BB=9AI CELLPHO=
# NES NGAY &gt;&gt;

#                                                     </a></td>

#                                             </tr>

#                                         </tbody>

#                                     </table></div>

#                             </td>

#                         </tr>

#                         <tr>

#                             <td align=3D"center" valign=3D"top" style=3D"ma=
# rgin: 0px; padding: 0px;" class=3D"responsive-cell">

#                                 <table border=3D"0" cellpadding=3D"0" cells=
# pacing=3D"0" align=3D"center" width=3D"100%" data-editable=3D"line" style=
# =3D"">

#                                     <tbody>

#                                         <tr>

#                                             <td valign=3D"top" align=3D"cen=
# ter" style=3D"padding: 10px 0px; margin: 0px;"><div style=3D"height: 1px; l=
# ine-height: 1px; border-top: 1px solid rgb(251, 18, 18);">

#                                                     <img src=3D"data:image/=
# gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=3D=3D=
# " alt=3D"" width=3D"1" height=3D"1" style=3D"display: block;" createnew=3D"=
# true">

#                                                 </div></td>

#                                         </tr>

#                                     </tbody>

#                                 </table>

#                             </td>

#                         </tr><tr><td align=3D"center" valign=3D"top" style=
# =3D"margin: 0px; padding: 0px;" class=3D"responsive-cell"><table width=3D"1=
# 00%" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" align=3D"center" data=
# -editable=3D"text" class=3D"text-block"><tbody><tr><td align=3D"left" valig=
# n=3D"top" class=3D"lh-1" style=3D"padding: 10px; font-size: 16px; font-fami=
# ly: 'Times New Roman', Times, serif; line-height: 1.15;"><div style=3D"text=
# -align: center;"><span style=3D"background-color: inherit; font-size: 23px;=
#  color: rgb(255, 0, 0); font-family: Arial, Helvetica, sans-serif; font-wei=
# ght: 700;">Tin t=E1=BB=A9c c=C3=B4ng ngh=E1=BB=87</span></div></td></tr></t=
# body></table></td></tr>

#                        =20

#                        =20

#                         <tr><td align=3D"center" valign=3D"top" style=3D"ma=
# rgin: 0px; padding: 0px;" class=3D"responsive-cell"><table cellpadding=3D"0=
# " cellspacing=3D"0" border=3D"0" width=3D"100%"><tbody><tr><td valign=3D"to=
# p" align=3D"left" width=3D"50%" style=3D"padding: 0px; margin: 0px;" class=
# =3D"responsive-cell"><table cellpadding=3D"0" cellspacing=3D"0" border=3D"0=
# " width=3D"100%"><tbody><tr><td style=3D"margin: 0px; padding: 0px;" align=
# =3D"center" valign=3D"top" class=3D"responsive-cell"><table width=3D"100%" =
# border=3D"0" cellpadding=3D"0" cellspacing=3D"0" align=3D"center" data-edit=
# able=3D"text" class=3D"text-block"><tbody><tr><td valign=3D"top" align=3D"l=
# eft" class=3D"lh-1" style=3D"padding: 10px; margin: 0px; font-size: 16px; f=
# ont-family: 'Times New Roman', Times, serif; line-height: 1.15;"><table bor=
# der=3D"0" cellpadding=3D"0" cellspacing=3D"0" align=3D"right" data-editable=
# =3D"image" style=3D"margin: 0px; padding: 0px;" data-mobile-stretch=3D"1" i=
# d=3D"edibkkb0" width=3D"285"><tbody><tr><td valign=3D"top" align=3D"left" s=
# tyle=3D"display: inline-block; padding: 0px 0px 10px 10px; margin: 0px;" cl=
# ass=3D"tdBlock responsive-cell"><a href=3D"https://inmail.inone.useinsider.=
# com/click.html?x=3Da62e&lc=3D81th&mc=3Du&s=3DksNEG&u=3DFt&z=3DczQSPjG&" tar=
# get=3D"_blank"><img src=3D"https://multimedia.inmail.inone.useinsider.com/i=
# nsider-BU/photos/0f668fe7-1558-48b5-ac17-8de070dacbe5.jpg?img1593081522304"=
#  width=3D"275" style=3D"border-width: 0px; border-style: none; border-color=
# : transparent; font-size: 12px; display: block;" data-src=3D"https://multim=
# edia.inmail.inone.useinsider.com/insider-BU/photos/0f668fe7-1558-48b5-ac17-=
# 8de070dacbe5.jpg|480|241|480|241|0|0|1.7454545454545454" height=3D"138" dat=
# a-origsrc=3D"https://multimedia.inmail.inone.useinsider.com/insider-BU/phot=
# os/5424949d-9915-4b7a-8609-a7e5ee354fb8.jpg" class=3D"mobile-image-stretch-=
# enabled"></a></td></tr></tbody></table><div><a href=3D"https://inmail.inone=
# .useinsider.com/click.html?x=3Da62e&lc=3D81th&mc=3Du&s=3DksNEG&u=3DFt&z=3Dc=
# qEMofl&" target=3D"_blank" title=3D"" style=3D"background-color: inherit; t=
# ext-decoration: none; color: rgb(0, 0, 0);"><br><font size=3D"15" style=3D"=
# font-size: 15px; font-family: Arial,'Helvetica Neue', Helvetica, sans-serif=
# ;"><span style=3D"background-color: transparent;">Ch=C3=A1y h=C3=A0ng ch=E1=
# =BB=89 sau 1 gi=E1=BB=9D m=E1=BB=9F b=C3=A1n, Galaxy S20+ BTS Edition c=C3=
# =B3 g=C3=AC m=C3=A0 h=E1=BA=A5p d=E1=BA=ABn =C4=91=E1=BA=BFn v=E1=BA=ADy?</=
# span>.............<span style=3D"background-color: transparent; font-weight=
# : bold; font-style: italic;">Xem th=C3=AAm &gt;&gt;</span></font></a><br></=
# div></td></tr></tbody></table></td></tr><tr><td style=3D"margin: 0px; paddi=
# ng: 0px;" align=3D"center" valign=3D"top" class=3D"responsive-cell"><table =
# width=3D"100%" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" align=3D"ce=
# nter" data-editable=3D"text" class=3D"text-block"><tbody><tr><td valign=3D"=
# top" align=3D"left" class=3D"lh-1" style=3D"padding: 10px; margin: 0px; fon=
# t-size: 16px; font-family: 'Times New Roman', Times, serif; line-height: 1.=
# 15;"><table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" align=3D"right=
# " data-editable=3D"image" style=3D"margin: 0px; padding: 0px;" data-mobile-=
# stretch=3D"1" id=3D"edibbboo" width=3D"285"><tbody><tr><td valign=3D"top" a=
# lign=3D"left" style=3D"display: inline-block; padding: 0px 0px 10px 10px; m=
# argin: 0px;" class=3D"tdBlock responsive-cell"><a href=3D"https://inmail.in=
# one.useinsider.com/click.html?x=3Da62e&lc=3D81tx&mc=3Du&s=3DksNEG&u=3DFt&z=
# =3DcqkgzuJ&" target=3D"_blank"><img src=3D"https://multimedia.inmail.inone.=
# useinsider.com/insider-BU/photos/11a4c455-8db0-4c79-8b9e-d56ac040d953.jpg?i=
# mg1593081522304" width=3D"275" style=3D"border-width: 0px; border-style: no=
# ne; border-color: transparent; font-size: 12px; display: block;" data-src=
# =3D"https://multimedia.inmail.inone.useinsider.com/insider-BU/photos/11a4c4=
# 55-8db0-4c79-8b9e-d56ac040d953.jpg|480|241|480|241|0|0|1.7454545454545454" =
# height=3D"138" data-origsrc=3D"https://multimedia.inmail.inone.useinsider.c=
# om/insider-BU/photos/89ed6145-027a-42a3-9d72-8712f7398edf.jpg" class=3D"mob=
# ile-image-stretch-enabled"></a></td></tr></tbody></table><font size=3D"15" =
# style=3D"font-size: 15px; font-family: Arial,'Helvetica Neue', Helvetica, s=
# ans-serif;"><a href=3D"https://inmail.inone.useinsider.com/click.html?x=3Da=
# 62e&lc=3D81tx&mc=3Du&s=3DksNEG&u=3DFt&z=3DcqDhoIi&" target=3D"_blank" title=
# =3D"" style=3D"text-decoration: none; color: rgb(0, 0, 0);">Tr=C3=AAn tay X=
# iaomi Mi Band 5 t=E1=BA=A1i VN: V=C3=B2ng =C4=91eo tay th=C3=B4ng minh kh=
# =C3=B4ng c=C3=B3 =C4=91=E1=BB=91i th=E1=BB=A7 trong ph=C3=A2n kh=C3=BAc d=
# =C6=B0=E1=BB=9Bi 1 tri=E1=BB=87u.....<span style=3D"text-decoration: none; =
# color: rgb(38, 38, 38);"><span style=3D"text-decoration: none; color: rgb(0=
# , 0, 0);">...</span><span style=3D"text-decoration: none; color: rgb(0, 0, =
# 0); font-weight: bold; font-style: italic;">Xem th=C3=AAm &gt;&gt;</span></=
# span></a></font></td></tr></tbody></table></td></tr></tbody></table></td><t=
# d valign=3D"top" align=3D"left" width=3D"50%" style=3D"padding: 0px; margin=
# : 0px;" class=3D"responsive-cell"><table cellpadding=3D"0" cellspacing=3D"0=
# " border=3D"0" width=3D"100%"><tbody><tr><td style=3D"margin: 0px; padding:=
#  0px;" align=3D"center" valign=3D"top" class=3D"responsive-cell"><table wid=
# th=3D"100%" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" align=3D"cente=
# r" data-editable=3D"text" class=3D"text-block"><tbody><tr><td valign=3D"top=
# " align=3D"left" class=3D"lh-1" style=3D"padding: 10px; margin: 0px; font-s=
# ize: 16px; font-family: 'Times New Roman', Times, serif; line-height: 1.15;=
# "><table border=3D"0" cellpadding=3D"0" cellspacing=3D"0" align=3D"right" d=
# ata-editable=3D"image" style=3D"margin: 0px; padding: 0px;" data-mobile-str=
# etch=3D"1" id=3D"edi9bbbp" width=3D"285"><tbody><tr><td valign=3D"top" alig=
# n=3D"left" style=3D"display: inline-block; padding: 0px 0px 10px 10px; marg=
# in: 0px;" class=3D"tdBlock responsive-cell"><a href=3D"https://inmail.inone=
# .useinsider.com/click.html?x=3Da62e&lc=3D81tO&mc=3Du&s=3DksNEG&u=3DFt&z=3Dc=
# 8Q82g2&" target=3D"_blank"><img src=3D"https://multimedia.inmail.inone.usei=
# nsider.com/insider-BU/photos/58d2f989-690e-4b63-8a0a-4080cfe8e936.jpg?img15=
# 93081522304" width=3D"275" style=3D"border-width: 0px; border-style: none; =
# border-color: transparent; font-size: 12px; display: block;" data-src=3D"ht=
# tps://multimedia.inmail.inone.useinsider.com/insider-BU/photos/58d2f989-690=
# e-4b63-8a0a-4080cfe8e936.jpg|480|241|480|241|0|0|1.7454545454545454" height=
# =3D"138" data-origsrc=3D"https://multimedia.inmail.inone.useinsider.com/ins=
# ider-BU/photos/d2440aa9-a068-4153-b402-cd4bc317ab09.jpg" class=3D"mobile-im=
# age-stretch-enabled"></a></td></tr></tbody></table><div><font size=3D"15" s=
# tyle=3D"font-size: 15px; font-family: Arial,'Helvetica Neue', Helvetica, sa=
# ns-serif;"><a href=3D"https://inmail.inone.useinsider.com/click.html?x=3Da6=
# 2e&lc=3D81tO&mc=3Du&s=3DksNEG&u=3DFt&z=3DcpRoz2m&" target=3D"_blank" title=
# =3D"" style=3D"text-decoration: none; color: rgb(0, 0, 0);">Khi n=C3=A0o Ap=
# ple s=E1=BA=BD ph=C3=A1t h=C3=A0nh b=E1=BA=A3n c=E1=BA=ADp nh=E1=BA=ADt iOS=
#  14 v=C3=A0 iPadOS 14 public beta?<span style=3D"text-decoration: none; col=
# or: rgb(0, 0, 0);">............</span><span style=3D"text-decoration: none;=
#  color: rgb(0, 0, 0); font-style: italic; font-weight: bold;">Xem th=C3=AAm=
#  &gt;&gt;</span></a></font><br></div></td></tr></tbody></table></td></tr><t=
# r><td style=3D"margin: 0px; padding: 0px;" align=3D"center" valign=3D"top" =
# class=3D"responsive-cell"><table width=3D"100%" border=3D"0" cellpadding=3D=
# "0" cellspacing=3D"0" align=3D"center" data-editable=3D"text" class=3D"text=
# -block"><tbody><tr><td valign=3D"top" align=3D"left" class=3D"lh-1" style=
# =3D"padding: 10px; margin: 0px; font-size: 16px; font-family: 'Times New Ro=
# man', Times, serif; line-height: 1.15;"><table border=3D"0" cellpadding=3D"=
# 0" cellspacing=3D"0" align=3D"right" data-editable=3D"image" style=3D"margi=
# n: 0px; padding: 0px;" data-mobile-stretch=3D"1" id=3D"edi5kbbk" width=3D"2=
# 85"><tbody><tr><td valign=3D"top" align=3D"left" style=3D"display: inline-b=
# lock; padding: 0px 0px 10px 10px; margin: 0px;" class=3D"tdBlock responsive=
# -cell"><a href=3D"https://inmail.inone.useinsider.com/click.html?x=3Da62e&l=
# c=3D81t4&mc=3Du&s=3DksNEG&u=3DFt&z=3Dcq00m4a&" target=3D"_blank"><img src=
# =3D"https://multimedia.inmail.inone.useinsider.com/insider-BU/photos/c6be3b=
# 1f-3d94-4773-b6a5-b2f70c90a53d.jpg?img1593081522304" width=3D"275" style=3D=
# "border-width: 0px; border-style: none; border-color: transparent; font-siz=
# e: 12px; display: block;" data-src=3D"https://multimedia.inmail.inone.usein=
# sider.com/insider-BU/photos/c6be3b1f-3d94-4773-b6a5-b2f70c90a53d.jpg|480|24=
# 1|480|241|0|0|1.7454545454545454" height=3D"138" data-origsrc=3D"https://mu=
# ltimedia.inmail.inone.useinsider.com/insider-BU/photos/e12e600e-1685-45c8-8=
# e62-eb6e2dbc3acd.jpg" class=3D"mobile-image-stretch-enabled"></a></td></tr>=
# </tbody></table><div><font style=3D"font-size: 14px; font-family: Arial,'He=
# lvetica Neue', Helvetica, sans-serif;" size=3D"14"><a href=3D"https://inmai=
# l.inone.useinsider.com/click.html?x=3Da62e&lc=3D81tI&mc=3Du&s=3DksNEG&u=3DF=
# t&z=3Dc9SlXfR&" target=3D"_blank" title=3D"" style=3D"text-decoration: none=
# ; color: rgb(0, 0, 0);"><br></a></font><a href=3D"https://inmail.inone.usei=
# nsider.com/click.html?x=3Da62e&lc=3D81t4&mc=3Du&s=3DksNEG&u=3DFt&z=3DcS97zl=
# P&" target=3D"_blank" title=3D"" style=3D"text-decoration: none; color: rgb=
# (0, 0, 0);"><font size=3D"15" style=3D"font-size: 15px; font-family: Arial,=
# 'Helvetica Neue', Helvetica, sans-serif;"><span style=3D"background-color: =
# transparent;">Th=C3=AAm b=E1=BA=B1ng ch=E1=BB=A9ng x=C3=A1c nh=E1=BA=ADn d=
# =C3=B2ng iPhone 12 series s=E1=BA=BD =C4=91=C6=B0=E1=BB=A3c t=E1=BA=B7ng k=
# =C3=A8m c=E1=BB=A7 s=E1=BA=A1c 20W......</span></font><span style=3D"backgr=
# ound-color: transparent; font-family: Arial,'Helvetica Neue', Helvetica, sa=
# ns-serif; font-size: 15px;">..............</span><font style=3D"font-family=
# : Arial,'Helvetica Neue', Helvetica, sans-serif; font-size: 15px;"><span st=
# yle=3D"color: rgb(0, 0, 0);">...</span><span style=3D"text-decoration: none=
# ; color: rgb(0, 0, 0); background-color: transparent;">.......</span><span =
# style=3D"text-decoration-line: none; color: rgb(0, 0, 0); background-color:=
#  transparent; font-weight: bold; font-style: italic;">Xem th=C3=AAm &gt;&gt=
# ;</span></font></a></div></td></tr></tbody></table></td></tr></tbody></tabl=
# e></td></tr></tbody></table></td></tr><tr>

#                             <td align=3D"center" valign=3D"top" style=3D"ma=
# rgin: 0px; padding: 0px;" class=3D"responsive-cell">

#                                 <table border=3D"0" cellpadding=3D"0" cells=
# pacing=3D"0" align=3D"center" width=3D"100%" data-editable=3D"line" style=
# =3D"">

#                                     <tbody>

#                                         <tr>

#                                             <td valign=3D"top" align=3D"cen=
# ter" style=3D"padding: 10px 0px; margin: 0px;"><div style=3D"height: 1px; l=
# ine-height: 1px; border-top: 1px solid rgb(251, 18, 18);">

#                                                     <img src=3D"data:image/=
# gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=3D=3D=
# " alt=3D"" width=3D"1" height=3D"1" style=3D"display: block;" createnew=3D"=
# true">

#                                                 </div></td>

#                                         </tr>

#                                     </tbody>

#                                 </table>

#                             </td>

#                         </tr><tr>

#                             <td align=3D"center" valign=3D"top" style=3D"ma=
# rgin: 0px; padding: 0px;" class=3D"responsive-cell">

#                                 <table cellpadding=3D"0" cellspacing=3D"0" =
# align=3D"center" data-editable=3D"image" data-mobile-stretch=3D"1" width=3D=
# "100%" style=3D"max-width: 100% !important;">

#                                     <tbody>

#                                         <tr>

#                                             <td valign=3D"top" align=3D"lef=
# t" style=3D"display: inline-block; padding: 10px 0px; margin: 0px;" class=
# =3D"tdBlock responsive-cell"><a href=3D"https://inmail.inone.useinsider.com=
# /click.html?x=3Da62e&lc=3D81td&mc=3Du&s=3DksNEG&u=3DFt&z=3DcQ2HSBk&" target=
# =3D"_blank"><img src=3D"https://multimedia.inmail.inone.useinsider.com/insi=
# der-BU/photos/88943123-5316-404c-86f2-550cffd207ee.jpg?img1593081522304" wi=
# dth=3D"601" data-src=3D"https://multimedia.inmail.inone.useinsider.com/insi=
# der-BU/photos/88943123-5316-404c-86f2-550cffd207ee.jpg|601|109|601|107|0|0|=
# 1" data-origsrc=3D"https://multimedia.inmail.inone.useinsider.com/insider-B=
# U/photos/bdde02a1-b580-4a1d-b2c4-c4fdcd710e53.jpg" class=3D"mobile-image-st=
# retch-enabled" style=3D"border-width: 0px; border-style: none; border-color=
# : transparent; font-size: 12px; display: block; width: 100%; max-width: 100=
# % !important;"></a></td>

#                                         </tr>

#                                     </tbody>

#                                 </table>

#                             </td>

#                         </tr>

#                         <tr>

#                             <td align=3D"center" valign=3D"top" style=3D"ma=
# rgin: 0px; padding: 0px;" class=3D"responsive-cell">

#                                 <table width=3D"100%" border=3D"0" cellpadd=
# ing=3D"0" cellspacing=3D"0" align=3D"center" data-editable=3D"text" class=
# =3D"text-block">

#                                     <tbody>

#                                         <tr>

#                                             <td align=3D"left" valign=3D"to=
# p" class=3D"lh-1" style=3D"padding: 10px; font-size: 16px; font-family: 'Ti=
# mes New Roman', Times, serif; line-height: 1.15;">

#                                                 <span style=3D"color: rgb(1=
# 28, 128, 128); font-family: Arial,'Helvetica Neue', Helvetica, sans-serif;"=
# >

#                                                     <font style=3D"font-siz=
# e: 9px;" size=3D"9">

#                                                         =C4=90=E1=BB=83 ng=
# =C6=B0ng nh=E1=BA=ADn Email t=E1=BB=AB CellphoneS, Qu=C3=BD kh=C3=A1ch vui =
# l=C3=B2ng nh=E1=BA=A5n <a href=3D"https://inmail.inone.useinsider.com/unsub=
# scribe.html?x=3Da62e&m=3Dq7F&mc=3Du&s=3DksNEG&u=3DFt&z=3DccCNz33&" target=
# =3D"_blank" title=3D"" style=3D"font-style: italic;">v=C3=A0o =C4=91=C3=A2y=
# </a>

#                                                     </font>

#                                                 </span>

#                                                 <br>

#                                             </td>

#                                         </tr>

#                                     </tbody>

#                                 </table>

#                             </td>

#                         </tr>

#                     </tbody>

#                 </table>

#             </td>

#         </tr>

#     </tbody>

# </table>
# </div></body>
# </html>"""

# from bs4 import BeautifulSoup
# import quopri

# soup = BeautifulSoup(tset, features="lxml")
# out = None

# ff = open("./tsst.txt", "ab")

# for f in soup.findAll():
#     ff.write(quopri.decodestring(f.text.encode()))

# ff.close()

from Crypto.IO import PEM
from Crypto.PublicKey import RSA

key = RSA.import_key("""-----BEGIN PUBLIC KEY-----
MIICIDANBgkqhkiG9w0BAQEFAAOCAg0AMIICCAKCAgEAuH0HV9CZiufvCQBYp66P
jYKzVIa9ixoK+y+UjdyDzi11iNbuEFUyOZRfMjV09IToTimHbVHI7a8nbQ3Q4pX3
6cxOU2CTQSN3Bt0jSNFCPCRvp1+Tq6jmvzN6gjmNizIAz4e3sygPB6Z1Rlk0p4Q6
5dZ2dAZLv2TBit3Fk6FOs57ubENAStlYZHYS9jS812YPtLqErlZcm+Cr+EvwuKiD
uJCQeMO7/CPcQLtWW2P/z+PfWvRQLiVhFJOS9npjpJTgahqZwoZPMZ+Glt+OP/tZ
pNXu8k9miC+nM+Ua4HAJmMdPEwF1L7SWDOodpuYLIG6oU7F/FfDJA3Zv2FxX23Bt
f6EmZhRwaBUjvHeHdo76e3ilBcOBLuVJVKne8ucMH5ykZEocx9nh2U69+faKm+gj
0v/jlVzcTtbDL1Da5/NHUJW+DVTwgcpipDkbd/cWaQtVzzjd6DhLgL6oNva9KF0d
OWTehKQuGj2XL6CNlHxTf2YwYpCPbjv/cwOsw2msguPRFBPHIx9hJSElJ8Cepjsm
ztp5z7DZk+rVRTYO+mxc12PbEMq9pVlaisw4NIl0iizNe0uDL/+mUx6dNfNLnA8G
DzTAN8QS7t774NvjVbrtbMXSB8B0gQAMvddaY021hGHAoFsUPrk2XhQ4PX/uI105
j8UUCsmHH7KPW1ij07erNqECAQU=
-----END PUBLIC KEY-----""")

key.