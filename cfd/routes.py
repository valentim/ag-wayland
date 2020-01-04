from controllers.diagram import diagram

def setup_routes(app):
    app.router.add_post('/diagrams', diagram.index)