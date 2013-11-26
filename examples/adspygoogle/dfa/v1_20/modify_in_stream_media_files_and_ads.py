#!/usr/bin/python
#
# Copyright 2013 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This example retrieves an In-Stream video creative and modifies its media
files, companion ads, and non-linear ads. You are not given the opportunity to
set the fields on these components when they are created by uploading creative
assets. Therefore, you must upload the assets first and then set any additional
fields in a second request.

To create an In-Stream video creative, run create_in_stream_video_creative.py.
To add an In-Stream asset to an In-Stream video creative, run
upload_in_stream_asset.py.

Tags: creative.saveCreative
"""

__author__ = 'api.jdilallo@gmail.com (Joseph DiLallo)'

import os
import sys
sys.path.insert(0, os.path.join('..', '..', '..', '..'))

# Import appropriate classes from the client library.
from adspygoogle import DfaClient


# Set the ID of the In-Stream video creative whose components will be updated.
CREATIVE_ID = 'INSERT_IN_STREAM_VIDEO_CREATIVE_ID_HERE'


def main(client, creative_id):
  # Initialize appropriate service.
  creative_service = client.GetCreativeService(
      'https://advertisersapitest.doubleclick.net', 'v1.20')

  # Fetch the In-Stream video creative which contains the asset to modify.
  in_stream_video_creative = creative_service.GetCreative(creative_id)

  if in_stream_video_creative['typeId'] != '29':
    print ('Unable to update creative with ID \'%s\': not an In-Stream video '
           'creative.' % creative_id)
  else:
    # Modify the media files, companion ads, and/or non-linear ads.
    if in_stream_video_creative['mediaFiles']:
      for media_file in in_stream_video_creative['mediaFiles']:
        media_file['pickedToServe'] = not media_file['pickedToServe']

    if in_stream_video_creative['companionAds']:
      for companion_ad in in_stream_video_creative['companionAds']:
        companion_ad['altText'] += ' Updated.'

    if in_stream_video_creative['linearAds']:
      for non_linear_ad in in_stream_video_creative['linearAds']:
        non_linear_ad['scalable'] = not non_linear_ad['scalable']

    result = creative_service.SaveCreative(in_stream_video_creative, 0)

    print ('Updated the In-Stream assets of In-Stream video creative with ID '
           '\'%s\'.' % result['id'])


if __name__ == '__main__':
  # Initialize client object.
  client = DfaClient(path=os.path.join('..', '..', '..', '..'))
  main(client, CREATIVE_ID)
