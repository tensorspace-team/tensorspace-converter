const tf = require( '@tensorflow/tfjs' );
require( '@tensorflow/tfjs-node' );
const Utils = require( "./utils/Utils" );
const SequentialConverter = require( "./encapsulation/Sequential" );
const FunctionalConverter = require( "./encapsulation/Functional" );

let options = process.argv;
let output_layer_names = undefined;
let input_path = undefined;
let output_path = undefined;

for ( let i = 2; i < options.length - 2; i ++ ) {

	let option = options[ i ];
	let parameters = option.split("=");

	if ( parameters[ 0 ] ===  "--output_layer_names" ) {

		output_layer_names = Utils.getOutputLayerNames( parameters[ 1 ] );

	}

}

input_path = Utils.getInputPath( options[ options.length - 2 ] );
output_path = Utils.getOutputPath( options[ options.length - 1 ] );

encapsulateModel();

async function encapsulateModel () {

	const model = await tf.loadModel( input_path );

	let encModel = SequentialConverter.encapsulate( model, output_layer_names );
	// let encModel = FunctionalConverter.encapsulate( model, output_layer_names );

	await encModel.save( output_path );

}