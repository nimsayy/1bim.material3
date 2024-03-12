@app.route('/usuario/<nome>')
def usuario(nome):

    return reuder_temolate('usuario.html',x=nome)

@app.route('/dobro,defalts={'n':1}')
@app.route('/dobro/<int:n>')
def dobro(n)

    r = 2*n
    return render_template('dobro.html',n=n,r=r)