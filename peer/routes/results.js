var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/result/#something', function (req, res, next) {
    res.sendfile('../public/start.html')
});

module.exports = router;