const tf = require( '@tensorflow/tfjs' );
require( '@tensorflow/tfjs-node' );

let options = process.argv;
let output_layer_names = undefined;
let input_path = undefined;
let output_path = undefined;

for ( let i = 2; i < options.length - 2; i ++ ) {

	let option = options[ i ];
	let parameters = option.split("=");

	if ( parameters[ 0 ] ===  "--output_layer_names" ) {

		output_layer_names = getOutputLayerNames( parameters[ 1 ] );

	}

}

input_path = getInputPath( options[ options.length - 2 ] );
output_path = getOutputPath( options[ options.length - 1 ] );

encapsulateModel();

function getOutputLayerNames( names ) {

	let output_layer_names = [];
	let nameInArray = names.split('/');

	for ( let i = 0; i < nameInArray.length; i ++ ) {

		output_layer_names.push( nameInArray[ i ] );

	}

	return output_layer_names;

}

function getInputPath( path ) {

	return 'file://' + path;

}

function getOutputPath( path ) {

	return 'file://' + path;

}

async function encapsulateModel () {

	const model = await tf.loadModel(input_path);

	let layers = model.layers;

	const input = model.inputs;
	let outputList = [];
	let tempInput = input;
	let tempOutput = null;

	let symbolicList = [ tempInput ];

	for (let i = 1; i < layers.length; i ++) {

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

	await encModel.save( output_path );

}