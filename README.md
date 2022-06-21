# Django-REST-Framework-sample
Django REST Frameworkを用いて簡易的なAPIを作成

＜環境構築手順＞
1.ライブラリをインストール
pip3 install django
pip3 install djangorestframework
pip3 install django-filter 

2.プロジェクト作成
django-admin startproject django_rest_framework_sample
cd django_rest_framework_sample/
python3 manage.py startapp blog

3.データベース作成
python3 manage.py makemigrations
python3 manage.py migrate

4.adminユーザ作成
python3 manage.py createsuperuser
password:***

5.サーバ起動
python3 manage.py runserver

6.管理画面を開く
http://localhost:8000/admin/

7.ユーザ側の画面を開く
http://127.0.0.1:8000/

8.REST APIを作成
・Serializer
・ViewSet
・URL pattern
