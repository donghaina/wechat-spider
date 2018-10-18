# coding = utf-8
import get_post_content
from flask import Flask, render_template, Markup, request, redirect

app = Flask('__name__')
app.config['SECRET_KEY'] = 'tww'


@app.route("/", methods=['GET', 'POST'])
def show_add_feed():
    if request.method == 'POST':
        wx_id = request.form.get('wx_id') or ''
        print(wx_id)
        scraping_time = request.form.get('scraping_time') or ''
        print(scraping_time)
        if wx_id == '':
            message = '微信公众号ID不能为空'
            return render_template('add_feed.html', message=message)
        else:
            message = '您所填写的微信公众号' + wx_id + '已保存'
            return render_template('add_feed.html', message=message)

    return render_template('add_feed.html')


@app.route("/post/1")
def show_post_content():
    post_content = Markup(get_post_content.get_post_content('2602994653214'))
    return render_template('show_post_content.html', post_content=post_content)


if __name__ == '__main__':
    app.debug = True
    app.run()
