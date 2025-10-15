// 7.b / 8.* myNotes app skeleton
const express = require('express');
const app = express();
const route = require('../routes/route');
const helmet = require('helmet');
const cookieParser = require('cookie-parser');
const session = require('express-session');

app.use(express.json());
app.use(helmet());
app.use(cookieParser());
app.use(session({ secret: 'demo-secret', resave:false, saveUninitialized:true }));

app.use('/', route);

app.listen(3000, ()=>console.log('myNotes app listening on 3000'));
