const express = require('express');
const app = express();
const bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.set('view engine', 'hbs');

app.get('/', (req, res) => {
    res.render('tweets');
});

app.post('/', (req, res) => {
    console.log(req.body);
    res.render('index');
});

app.listen(3000, () => {
    console.log('Server started on port 3000');
});