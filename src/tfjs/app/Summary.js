const tf = require( '@tensorflow/tfjs' );
require( '@tensorflow/tfjs-node' );

async function showSummary( input_path ) {

    const model = await tf.loadModel( input_path );
    model.summary();

}

exports.showSummary = showSummary;