const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const axios = require('axios');
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.set('view engine', 'hbs');

app.get('/', (req, res) => {
    res.render('tweets');
});

app.post('/', (req, res) => {
    console.log(req.body);
    res.render('tweets');
});
app.post('/addTwitter', (req, res) => {
    console.log(req.body);
    axios.post("http://127.0.0.1:5000/receiver", 
    {
    // method: 'POST',
    // headers: {
    // 'Content-type': 'application/json',
    // 'Accept': 'application/json'
    // },
    // Strigify the payload into JSON:
    body:JSON.stringify(req.body)}).then(res=>{
    if(res.ok){
    return res.json()
    }else{
    alert("something is wrong")
    }
    }).then(jsonResponse=>{
    
    // Log the response data in the console
    console.log(jsonResponse)
    } 
    ).catch((err) => console.error(err));
    
    
    res.render('tweets');
});

app.listen(3000, () => {
    console.log('Server started on port 3000');
});