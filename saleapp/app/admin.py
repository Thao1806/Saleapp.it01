from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from saleapp.app.Models import Categories, Product
from saleapp.app import app, db

admin = Admin(app=app, name="Quản trị bán hàng", template_mode='bootstrap4')


class MyProductView(ModelView):
    column_list = ['id', 'name', 'price']
    can_export = True
    column_searchable_list = ['name', 'price']
    column_filters = ['name', 'price']
    column_editable_list = ['name', 'price']
    edit_modal = True


class MyCategoryView(ModelView):
    column_list = ['name', 'Product']

class MyStatsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/stas.html')

admin.add_view(MyCategoryView(Categories, db.session))
admin.add_view(MyProductView(Product, db.session))
admin.add_view(MyStatsView(name='Thông tin báo cáo'))
