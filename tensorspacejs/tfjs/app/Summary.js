/**
 * @author syt123450 / https://github.com/syt123450
 */

const tf = require( '@tensorflow/tfjs' );
require( '@tensorflow/tfjs-node' );

async function showSummary( input_path ) {

    const model = await tf.loadModel( input_path );
    model.summary();

}

exports.showSummary = showSummary;