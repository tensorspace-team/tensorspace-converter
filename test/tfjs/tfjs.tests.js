const chai = require("chai");
const tf = require("@tensorflow/tfjs");
require("@tensorflow/tfjs-node");
const rimraf = require("rimraf");
const shell = require("shelljs");

const OUTPUT_DIR = "./test/output/";

describe('Test Convert TensorFlow.js Models', function () {

	it('Test Sequential model', async function () {

		const startMemory = await tf.memory();

		// Execute converter script to convert TensorFlow.js model.
		shell.exec('./test/tfjs/sequential/test.sh');

		// Load converted model for test, TensorFlow.js model will be converted to layer model.
		const model = await tf.loadLayersModel('file://' + OUTPUT_DIR + 'model.json');

		const randomInput = tf.randomNormal([1, 28, 28, 1]);
		const result = model.predict(randomInput);

		// Test converted model outputs.
		chai.expect( result[0].shape ).to.eql( [ 1, 32, 32, 1 ] );
		chai.expect( result[1].shape ).to.eql( [ 1, 28, 28, 6 ] );
		chai.expect( result[2].shape ).to.eql( [ 1, 14, 14, 6 ] );
		chai.expect( result[3].shape ).to.eql( [ 1, 10, 10, 16 ] );
		chai.expect( result[4].shape ).to.eql( [ 1, 5, 5, 16 ] );
		chai.expect( result[5].shape ).to.eql( [ 1, 120 ] );
		chai.expect( result[6].shape ).to.eql( [ 1, 84 ] );
		chai.expect( result[7].shape ).to.eql( [ 1, 10 ] );

		tf.dispose(model);
		tf.dispose(randomInput);
		tf.dispose(result);

		// Remove generated model files.
		rimraf.sync(OUTPUT_DIR);

		const endMemory = await tf.memory();

		// Ensure no memory leak.
		chai.expect( startMemory.numTensors ).to.equal( endMemory.numTensors );

	});

});