

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """

hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
'''

fix_sidebar= """
<style>
[data-testid="stSidebar"][aria-expanded="true"] > div:first-child {width: 320px;}
[data-testid="stSidebar"][aria-expanded="false"] > div:first-child {width: 320px;margin-left: -320px;}
</style>
"""

fix_tabs= """
<style>
button[data-baseweb="tab"] {
  font-size: 20px;
}
</style>


"""
hide_top_padding = """
    <style>
        div.block-container {padding-top:0.1rem;}
    </style>
"""
 