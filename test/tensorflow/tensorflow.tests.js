const chai = require("chai");
const tf = require("@tensorflow/tfjs");
require("@tensorflow/tfjs-node");
const rimraf = require("rimraf");
const shell = require("shelljs");

const OUTPUT_DIR = "./test/output/";

describe('Test Convert TensorFlow Models', function () {

	it('Test Frozen model', async function () {

	    const startMemory = await tf.memory();
		
		// Execute converter script to convert Frozen model.
		shell.exec('./test/tensorflow/frozenModel/test.sh');
		
		// Load converted model for test,  frozen model will be converted to graph model.
		const model = await tf.loadGraphModel('file://' + OUTPUT_DIR + 'model.json');

		const randomInput = tf.randomNormal([1, 28, 28, 1]);
		const result = model.execute(
			randomInput,
			[
				"MyConv2D_1",
				"MyMaxPooling2D_1",
				"MyConv2D_2",
				"MyMaxPooling2D_2",
				"MyDense_1",
				"MyDense_2",
				"MySoftMax"
			]
		);
		
		// Test converted model outputs.
		chai.expect( result[0].shape ).to.eql( [ 1, 24, 24, 6 ] );
		chai.expect( result[1].shape ).to.eql( [ 1, 12, 12, 6 ] );
		chai.expect( result[2].shape ).to.eql( [ 1, 8, 8, 16 ] );
		chai.expect( result[3].shape ).to.eql( [ 1, 4, 4, 16 ] );
		chai.expect( result[4].shape ).to.eql( [ 1, 120 ] );
		chai.expect( result[5].shape ).to.eql( [ 1, 84 ] );
		chai.expect( result[6].shape ).to.eql( [ 1, 10 ] );

		tf.dispose(model);
		tf.dispose(randomInput);
		tf.dispose(result);
		
		// Remove generated model files.
		rimraf.sync(OUTPUT_DIR);

		const endMemory = await tf.memory();
		
		// Ensure no memory leak.
		chai.expect( startMemory.numTensors ).to.equal( endMemory.numTensors );

	});

	it('Test Saved Model', async function () {

	    const startMemory = await tf.memory();
		
		// Execute converter script to saved Frozen model.
		shell.exec('./test/tensorflow/savedModel/test.sh');
		
		// Load converted model for test, saved model will be converted to graph model.
		const model = await tf.loadGraphModel('file://' + OUTPUT_DIR + 'model.json');

		const randomInput = tf.randomNormal([1, 28, 28, 1]);
		const result = model.execute(
			randomInput,
			[
				"MyConv2D_1",
				"MyMaxPooling2D_1",
				"MyConv2D_2",
				"MyMaxPooling2D_2",
				"MyDense_1",
				"MyDense_2",
				"MySoftMax"
			]
		);
		
		// Test converted model outputs.
		chai.expect( result[0].shape ).to.eql( [ 1, 24, 24, 6 ] );
		chai.expect( result[1].shape ).to.eql( [ 1, 12, 12, 6 ] );
		chai.expect( result[2].shape ).to.eql( [ 1, 8, 8, 16 ] );
		chai.expect( result[3].shape ).to.eql( [ 1, 4, 4, 16 ] );
		chai.expect( result[4].shape ).to.eql( [ 1, 120 ] );
		chai.expect( result[5].shape ).to.eql( [ 1, 84 ] );
		chai.expect( result[6].shape ).to.eql( [ 1, 10 ] );

		tf.dispose(model);
		tf.dispose(randomInput);
		tf.dispose(result);
		
		// Remove generated model files.
		rimraf.sync(OUTPUT_DIR);

		const endMemory = await tf.memory();
		
		// Ensure no memory leak.
		chai.expect( startMemory.numTensors ).to.equal( endMemory.numTensors );

	});

	it('Test tf.keras Model', async function () {

	    const startMemory = await tf.memory();
		
		// Execute converter script to tf.keras model.
		shell.exec('./test/tensorflow/combinedKeras/test.sh');
		
		// Load converted model for test, tf.keras model will be converted to layer model.
		const model = await tf.loadLayersModel('file://' + OUTPUT_DIR + 'model.json');

		const randomInput = tf.randomNormal([1, 28, 28]);
		const result = model.predict(randomInput);
		
		// Test converted model outputs.
		chai.expect( result[0].shape ).to.eql( [ 1, 24, 24, 6 ] );
		chai.expect( result[1].shape ).to.eql( [ 1, 12, 12, 6 ] );
		chai.expect( result[2].shape ).to.eql( [ 1, 8, 8, 16 ] );
		chai.expect( result[3].shape ).to.eql( [ 1, 4, 4, 16 ] );
		chai.expect( result[4].shape ).to.eql( [ 1, 120 ] );
		chai.expect( result[5].shape ).to.eql( [ 1, 84 ] );
		chai.expect( result[6].shape ).to.eql( [ 1, 10 ] );

		tf.dispose(model);
		tf.dispose(randomInput);
		tf.dispose(result);
		
		// Remove generated model files.
		rimraf.sync(OUTPUT_DIR);

		const endMemory = await tf.memory();
		
		// Ensure no memory leak.
		chai.expect( startMemory.numTensors ).to.equal( endMemory.numTensors );

	});

	it('Test tf.keras Model, topology and weights saved in separated files', async function () {

	    const startMemory = await tf.memory();
		
		// Execute converter script to tf.keras model.
		shell.exec('./test/tensorflow/separatedKeras/test.sh');
		
		// Load converted model for test, tf.keras model will be converted to layer model.
		const model = await tf.loadLayersModel('file://' + OUTPUT_DIR + 'model.json');

		const randomInput = tf.randomNormal([1, 28, 28]);
		const result = model.predict(randomInput);
		
		// Test converted model outputs.
		chai.expect( result[0].shape ).to.eql( [ 1, 24, 24, 6 ] );
		chai.expect( result[1].shape ).to.eql( [ 1, 12, 12, 6 ] );
		chai.expect( result[2].shape ).to.eql( [ 1, 8, 8, 16 ] );
		chai.expect( result[3].shape ).to.eql( [ 1, 4, 4, 16 ] );
		chai.expect( result[4].shape ).to.eql( [ 1, 120 ] );
		chai.expect( result[5].shape ).to.eql( [ 1, 84 ] );
		chai.expect( result[6].shape ).to.eql( [ 1, 10 ] );

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