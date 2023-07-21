#  def heading_two(text):
#      html=f"<h2>{text}</h2>"
#      return html
#  data = heading_two("This is heading two")
#  print(data)
#  data = heading_two("This is another heading two")
#  print(data)
#
#
# def heading_two(text):
#
#     """
#     return heading two text of html
#     :param text: Any kind of string
#     :return: html tag
#     """
#
#     html =f"<h2>{text}</h2>"
#     return html
#
# print(heading_two.__doc__)

def html_heading(text,html_tag):
    """
    Reture HTML tag of any text
    :param text:Any kind of string
    :param html_tag:What kind of html tag you want to generate
    :return: HTML tag of any text
    """
    html=f"<{html_tag}>{text}</{html_tag}>"
    return html
print(html_heading("this is paragraph"))