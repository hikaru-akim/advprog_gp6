@app.route('/purchase')
def purchase():
    if 'logged_in' in session and session['logged_in']:
        user_cart = users[session['username']]["cart"]
        total_price = sum(book["price"] for book in user_cart)
        users[session['username']]["cart"] = []
        flash(f'Purchase successful! Total: ${total_price}', 'success')
    else:
        flash('Please log in to make a purchase.', 'danger')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
