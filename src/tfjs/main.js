const tf = require( '@tensorflow/tfjs' );
require( '@tensorflow/tfjs-node' );
const Utils = require( "./utils/Utils" );
const FunctionalWrapper = require( "./wrapper/Functional" );
const SequentialWrapper = require( "./wrapper/Sequential" );

let options = process.argv;
let output_layer_names = undefined;
let input_path = undefined;
let output_path = undefined;

let exclude_input = false;

for ( let i = 2; i < options.length - 2; i ++ ) {

	let option = options[ i ];
	let parameters = option.split("=");

	if ( parameters[ 0 ] ===  "--output_layer_names" ) {

		output_layer_names = Utils.getOutputLayerNames( parameters[ 1 ] );

	} else if ( parameters[ 0 ] === "--exclude_input" ) {

		exclude_input = true;

	}

}

input_path = Utils.getInputPath( options[ options.length - 2 ] );
output_path = Utils.getOutputPath( options[ options.length - 1 ] );

encapsulateModel();

async function encapsulateModel () {

	const model = await tf.loadModel( input_path );

	let modelType = model.toJSON(null, false).class_name;

	console.log( modelType );

	let encModel;

	if ( modelType === "Model" ) {

		encModel = FunctionalWrapper.wrap( model, output_layer_names );

	} else {

		encModel = SequentialWrapper.wrap( model, output_layer_names, exclude_input );

	}

	await encModel.save( output_path );

}