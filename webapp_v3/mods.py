

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
[data-testid="stSidebar"][aria-expanded="true"] > div:first-child {width: 350px;}
[data-testid="stSidebar"][aria-expanded="false"] > div:first-child {width: 350px;margin-left: -350px;}
</style>
"""
