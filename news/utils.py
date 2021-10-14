class MyMixin(objects):
    mixin_prop = ""

    def get_prop(self):
        return  self.mixin_prop.upper()