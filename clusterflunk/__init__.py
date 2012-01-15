from pyramid.config import Configurator

def main(global_config, **settings):
        '''Main config function'''
        config = Configurator(settings=settings,
                              root_factory=Site,
                              request_factory=D2Request)
                          
        config.scan('clusterflunk')
        return config.make_wsgi_app()

if __name__ == '__main__':
    from paste.httpserver import serve
    serve(main(), host="0.0.0.0", port="5015")