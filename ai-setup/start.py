from .features.clone_ui import clone_ui
from .features.clone_ui.tools import get_website_css, get_website_screenshot
from .ui import show_title
show_title()
print(get_website_screenshot("http://motherduck.com/"))