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

    const model = await tf.loadLayersModel( input_path );

	let encModel;

	if ( hasOutputConfig ) {

		encModel = Wrapper.wrapWithName( model, output_layer_names );

	} else {

		encModel = Wrapper.wrapWithoutName( model );

	}

	await encModel.save( output_path );

}

exports.encapsulateModel = encapsulateModel;