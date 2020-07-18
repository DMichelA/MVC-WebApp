import web

urls = (
    '/', 'mvc.controllers.index.Index',
    
    '/alumnos_delete', 'mvc.controllers.alumnos.delete.Delete',
    '/alumnos_insert', 'mvc.controllers.alumnos.insert.Insert',
    '/alumnos_list', 'mvc.controllers.alumnos.list.List',
    '/alumnos_update', 'mvc.controllers.alumnos.update.Update',
    '/alumnos_view', 'mvc.controllers.alumnos.view.View',
)
app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()