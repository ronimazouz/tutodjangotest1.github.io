
var FilePreview = {

    /**
     * Get image orientation from EXIF info
     *
     * @param  File     file     File object retrieved from input
     * @param  Function callback Closure to call after complete
     * @return Integer           EXIF orientation value:
     *
     *                           # | Transform
     *                           --+----------------
     *                           2 | Flip Horizontal
     *                           3 | Rotate 180
     *                           4 | Flip Vertical
     *                           5 | Transpose
     *                           6 | Rotate 90
     *                           7 | Transverse
     *                           8 | Rotate 270
     *                           * | No Transform
     */
    getOrientation: function(file, callback) {
        var reader = new FileReader();

        reader.onload = function(e) {
            var view = new DataView(e.target.result);

            if (view.getUint16(0, false) != 0xFFD8) {
                return callback(-2);
            }

            var length = view.byteLength, offset = 2;
            while (offset < length) {
                if (view.getUint16(offset+2, false) <= 8) return callback(-1);
                var marker = view.getUint16(offset, false);
                offset += 2;
                if (marker == 0xFFE1) {
                    if (view.getUint32(offset += 2, false) != 0x45786966) {
                        return callback(-1);
                    }
                    var little = view.getUint16(offset += 6, false) == 0x4949;
                    offset += view.getUint32(offset + 4, little);
                    var tags = view.getUint16(offset, little);
                    offset += 2;
                    for (var i = 0; i < tags; i++) {
                        if (view.getUint16(offset + (i * 12), little) == 0x0112) {
                            return callback(view.getUint16(offset + (i * 12) + 8, little));
                        }
                    }
                } else if ((marker & 0xFF00) != 0xFF00) {
                    break;
                } else {
                    offset += view.getUint16(offset, false);
                }
            }

            return callback(-1);
        };

        reader.readAsArrayBuffer(file);
    },

    /**
     * Returns transform angle based on EXIF orientation.
     * Only rotation are considered here.
     *
     * @param  Integer Transform angle in degrees
     * @return Integer
     */
    getTransformAngle: function(orientation) {
        switch (orientation) {
            case 3: return 180; // Rotate 180
            case 6: return 90;
            case 8: return 270;
        }
        return 0;
    },

    /**
     * Load preview based on file, and apply transform angle
     *
     * @param  DOMElement $preview Preview DOMElement, selector or jQuery object
     * @param  File       file     File object retrieved from input
     * @param  Integer    angle    Angle to rotate in degrees
     */
    loadPreview: function($preview, file, angle) {
        var reader = new FileReader();
        reader.onload = function(e) {
            $preview.css({
                backgroundImage: "url('" + e.target.result + "')",
                transform: "rotate(" + angle + "deg)",
            });
            $preview.hide();
            $preview.fadeIn(650);
        };
        reader.readAsDataURL(file);
    },

    /**
     * Execute preview after a change event on a file input
     *
     * @param  mixed $input   Input file DOMElement, selector or jQuery object
     * @param  mixed $preview Preview file DOMElement, selector or jQuery object
     */
    preview: function($input, $preview) {
        var self = this;

        $input = $($input);
        $preview = $($preview);

        if (!$input[0].files || !$input[0].files[0]) {
            return;
        }

        var file = $input[0].files[0];

        // We get the orientation from EXIF info
        this.getOrientation(file, function(orientation) {
            // Convert this orientation to an angle for a CSS rotate transform
            var angle = self.getTransformAngle(orientation);
            // Then load the preview, applying this rotation
            self.loadPreview($preview, file, angle);
        });
    }

};

$("#imageUpload").change(function() {
    FilePreview.preview(this, "#imagePreview");
});
