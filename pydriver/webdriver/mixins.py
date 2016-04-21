class _BaseElementMixin(object):
    def get_web_element(self):
        return getattr(self, 'web_element')


class Disableable(_BaseElementMixin):
    def is_enabled(self):
        return self.get_web_element().is_enabled()


class Clickable(_BaseElementMixin):
    def click(self):
        return self.get_web_element().click()
