const tf = require( '@tensorflow/tfjs' );
require( '@tensorflow/tfjs-node' );
const Wrapper = require( "../wrapper/ModelWrapper" );

async function encapsulateModel(

    input_path,
    output_path,
    output_layer_names,
    hasOutputConfig

) {

    const model = await tf.loadModel( input_path );

	let encModel;

	if ( hasOutputConfig ) {

		encModel = Wrapper.wrapWithName( model, output_layer_names );

	} else {

		encModel = Wrapper.wrapWithoutName( model );

	}

	await encModel.save( output_path );

}

exports.encapsulateModel = encapsulateModel;