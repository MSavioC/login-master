from django.contrib.auth.models import User
user = User.objects.create_user(
    username='usuario_tester',
    email='teste@example.com',
    password='senha123'
)
print("usuario criado com sucesso:", user)