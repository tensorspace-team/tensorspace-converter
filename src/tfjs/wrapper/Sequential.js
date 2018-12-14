const tf = require( '@tensorflow/tfjs' );
require( '@tensorflow/tfjs-node' );

function wrap( model, output_layer_names, exclude_input ) {

	const input = model.inputs;
	let outputList = [];

	if ( !exclude_input ) {

	    outputList.push( input[ 0 ] );

    }

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

exports.wrap = wrap;