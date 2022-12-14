from flask import Blueprint, render_template

from classes.manager import DataManager


user_feed_blueprint = Blueprint('user_feed_blueprint', __name__)

PATH_DATA = "../app/data/data.json"
PATH_COMMENTS = "../app/data/comments.json"

data_manager = DataManager(PATH_DATA, PATH_COMMENTS)

@user_feed_blueprint.route('/users/<username>')
def user_feed(username):
    posts_by_user = data_manager.get_posts_by_user(username)
    return render_template('user-feed.html', posts_by_user=posts_by_user)