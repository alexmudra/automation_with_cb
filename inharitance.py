import io


class HtmlTag:
    def __init__(self, name: str, attributes: dict = dict(), style: dict = dict(), has_close_subtag: bool = True):
        # TAG name
        self.__name = name.upper()
        # Does tag have close part like <HTML></HTML>?
        self.has_close_subtag = has_close_subtag
        # HTML TAG attributes
        self.attributes = attributes
        # HTML TAG CSS style
        self.style = style
        # What is between opening ang close subtags
        self.__content = io.StringIO()

    @property
    def name(self):
        return self.__name

    @property
    def content(self):
        return self.__content.getvalue()

        # Setting HTML TAG attribute

    def set_attribute(self, name, value):
        self.attributes[name] = value
        return self

    # Set new CSS style
    def set_style(self, name, value):
        self.style[name] = value
        return self

    # Add text content into the text
    def add_content(self, content):
        self.__content.write(content)
        return self

    # Clear the tag content
    def clear_content(self):
        self.__content = io.StringIO()
        return self

    # Show TAG as is
    def show(self):
        tag_io = io.StringIO()
        opening = r'<'
        close_opening = r'</'
        closing = r'>'
        tag_io.write(f'{opening}{self.__name}')

        if self.attributes:
            tag_io.write(
                ' ' + ' '.join([f'{attr_key}="{self.attributes[attr_key]}"' for attr_key in self.attributes.keys()]))

        if self.style:
            tag_io.write(
                ' style="' + '; '.join([f'{style_key}: {self.style[style_key]}' for style_key in self.style.keys()]))

        tag_io.write(closing)

        if self.has_close_subtag:
            tag_io.write(self.content)
            tag_io.write(f'{close_opening}{self.__name}{closing}')

        return tag_io.getvalue()