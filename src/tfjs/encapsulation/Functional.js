const tf = require( '@tensorflow/tfjs' );
require( '@tensorflow/tfjs-node' );

function encapsulate( model, output_layer_names ) {

	let layers = model.layers;

	const input = model.inputs;
	let outputList = [];
	let tempInput = input;
	let tempOutput = null;

	let symbolicList = [ tempInput ];

	for ( let i = 1; i < layers.length; i ++ ) {

		tempOutput = layers[ i ].apply( tempInput );
		symbolicList.push( tempOutput );
		tempInput = tempOutput;

	}

	for ( let i = 0; i < output_layer_names.length; i ++ ) {

		let layerId = model.getLayer( output_layer_names[ i ] ).id;
		outputList.push( symbolicList[ layerId ] );

	}

	const encModel = tf.model( {

		inputs: input,
		outputs: outputList

	} );

	return encModel;

}

exports.encapsulate = encapsulate;