const chai = require("chai");
const tf = require("@tensorflow/tfjs");
require("@tensorflow/tfjs-node");
const rimraf = require("rimraf");
const shell = require("shelljs");

const OUTPUT_DIR = "./test/output/";

describe('Test Convert Keras Models', function () {

	it('Topology and weights saved in a same hdf5 file', async function () {

	    const startMemory = await tf.memory();

		shell.exec('./test/keras/combined/test_with_oln.sh');

		const model = await tf.loadLayersModel('file://' + OUTPUT_DIR + 'model.json');

		const randomInput = tf.randomNormal([1, 28, 28]);
		const result = model.predict(randomInput);

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

		rimraf.sync(OUTPUT_DIR);

		const endMemory = await tf.memory();

		chai.expect( startMemory.numTensors ).to.equal( endMemory.numTensors );

	});

	it('Topology and weights saved in a separated files', async function () {

	    const startMemory = await tf.memory();

		shell.exec('./test/keras/separated/test_separated.sh');

		const model = await tf.loadLayersModel('file://' + OUTPUT_DIR + 'model.json');

		const randomInput = tf.randomNormal([1, 28, 28]);
		const result = model.predict(randomInput);

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

		rimraf.sync(OUTPUT_DIR);

		const endMemory = await tf.memory();

		chai.expect( startMemory.numTensors ).to.equal( endMemory.numTensors );

	});

});