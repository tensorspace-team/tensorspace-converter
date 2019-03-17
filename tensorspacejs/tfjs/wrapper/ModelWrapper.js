/**
 * @author syt123450 / https://github.com/syt123450
 */

const tf = require( '@tensorflow/tfjs' );
require( '@tensorflow/tfjs-node' );

function wrapWithName( model, output_layer_names ) {

	const input = model.inputs;
	let outputList = [];

	for ( let i = 0; i < output_layer_names.length; i ++ ) {

		let layer = model.getLayer( output_layer_names[ i ] );

		let outputTensor = layer.output;

		outputList.push( outputTensor );

	}

	const encModel = tf.model( {

		inputs: input,
		outputs: outputList

	} );

	return encModel;

}

function wrapWithoutName( model ) {

	const input = model.inputs;
	let outputList = [];

	let layers = model.layers;

	for ( let i = 0; i < layers.length; i ++ ) {

		let outputTensor = layers[ i ].output;

		outputList.push( outputTensor );

	}

	const encModel = tf.model( {

		inputs: input,
		outputs: outputList

	} );

	return encModel;

}

exports.wrapWithName = wrapWithName;
exports.wrapWithoutName = wrapWithoutName;