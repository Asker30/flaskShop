from Store import store
from Store import views, admin
from Forum import forum

if __name__ == '__main__':
    store.run(debug=True)
    forum.run(debug=True)