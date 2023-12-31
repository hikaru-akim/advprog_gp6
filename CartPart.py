@app.route('/add_to_cart/<int:book_id>')
def add_to_cart(book_id):
    if 'logged_in' in session and session['logged_in']:
        book = next((b for b in books if b['id'] == book_id), None)
        if book:
            users[session['username']]["cart"].append(book)
            flash(f'{book["title"]} added to your cart!', 'success')
        else:
            flash('Book not found.', 'danger')
    else:
        flash('Please log in to add items to your cart.', 'danger')

    return redirect(url_for('index'))

@app.route('/cart')
def view_cart():
    if 'logged_in' in session and session['logged_in']:
        user_cart = users[session['username']]["cart"]
        return render_template('cart.html', cart=user_cart)
    else:
        flash('Please log in to view your cart.', 'danger')
        return redirect(url_for('login'))