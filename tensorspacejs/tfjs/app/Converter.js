/**
 * @author syt123450 / https://github.com/syt123450
 */

const tf = require( '@tensorflow/tfjs' );
require( '@tensorflow/tfjs-node' );
const Wrapper = require( "../wrapper/ModelWrapper" );

async function encapsulateModel(

    input_path,
    output_path,
    output_layer_names,
    hasOutputConfig

) {

	console.log( "Loading tfjs model..." );
    const model = await tf.loadLayersModel( input_path );

	let encModel;

	console.log( "Generating multi-output model..." );
	if ( hasOutputConfig ) {

		encModel = Wrapper.wrapWithName( model, output_layer_names );

	} else {

		encModel = Wrapper.wrapWithoutName( model );

	}

	console.log( "Saving generated model..." );
	await encModel.save( output_path );

}

exports.encapsulateModel = encapsulateModel;