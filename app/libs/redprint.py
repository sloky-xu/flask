

class Redprint:
    def __init__(self, name):
        """
        实例化红图对象
        :param name: 红图的名称
        """
        self.name = name
        self.mount = []

    def route(self, rule, **options):
        """
        实现红图的route装饰器
        :param rule: url
        :param options:
        :return:
        """
        def decorator(f):
            self.mount.append((f, rule, options))
            return f
        return decorator

    def register(self, bp, url_prefix=None):
        """
        注册红图
        :param bp: 蓝图对象
        :param url_prefix: url前缀，前缀为空时，就用实例化红图时传的name
        """
        if url_prefix is None:
            url_prefix = '/' + self.name

        for f, rule, options in self.mount:
            endpoint = options.pop("endpoint", None)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)
