#!/usr/bin/env node
// From Blinks various LEDs
const Blynk = require('/usr/lib/node_modules/blynk-library');
const b = require('bonescript');
const util = require('util');

const LED0 = 'USR3';//const LED0 = 'GREEN';
const button = 'P9_15';//const button = 'GP1_3';
const LED1 = 'P9_14';
b.pinMode(LED0, b.OUTPUT);
b.pinMode(button, b.INPUT);
b.pinMode(LED1, b.OUTPUT);

const AUTH = '708b34efa0d644cb841c6e3a992cae77';

var blynk = new Blynk.Blynk(AUTH);

var v0 = new blynk.VirtualPin(0);
var v10 = new blynk.WidgetLED(10);
var v2 =  new blynk.VirtualPin(2);
// console.log(util.inspect(v1));
// var v9 = new blynk.VirtualPin(9);

v0.on('write', function(param) {
    console.log('V0:', param[0]);
    b.digitalWrite(LED0, param[0]);
});

v2.on('write', function(param) {
    b.analogWrite(LED1, param[0]);
});

v10.setValue(0);    // Initially off

// v9.on('read', function() {
//     v9.write(new Date().getSeconds());
// });

b.attachInterrupt(button, toggle, b.CHANGE);

function toggle(x) {
    console.log("V1: ", x.value);
    x.value ? v10.turnOn() : v10.turnOff();
}
