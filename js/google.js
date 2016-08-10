var casper = require('casper').create();
 
casper.start('http://google.com/', function() {
    this.capture('google.png');
});
casper.run();
