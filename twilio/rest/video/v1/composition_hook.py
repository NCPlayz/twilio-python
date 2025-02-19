# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class CompositionHookList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the CompositionHookList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.video.v1.composition_hook.CompositionHookList
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookList
        """
        super(CompositionHookList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/CompositionHooks'.format(**self._solution)

    def stream(self, enabled=values.unset, date_created_after=values.unset,
               date_created_before=values.unset, friendly_name=values.unset,
               limit=None, page_size=None):
        """
        Streams CompositionHookInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param bool enabled: Read only CompositionHook resources with an enabled value that matches this parameter
        :param datetime date_created_after: Read only CompositionHook resources created on or after this ISO 8601 datetime with time zone
        :param datetime date_created_before: Read only CompositionHook resources created before this ISO 8601 datetime with time zone
        :param unicode friendly_name: Read only CompositionHook resources with friendly names that match this string
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.video.v1.composition_hook.CompositionHookInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            enabled=enabled,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            friendly_name=friendly_name,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, enabled=values.unset, date_created_after=values.unset,
             date_created_before=values.unset, friendly_name=values.unset,
             limit=None, page_size=None):
        """
        Lists CompositionHookInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param bool enabled: Read only CompositionHook resources with an enabled value that matches this parameter
        :param datetime date_created_after: Read only CompositionHook resources created on or after this ISO 8601 datetime with time zone
        :param datetime date_created_before: Read only CompositionHook resources created before this ISO 8601 datetime with time zone
        :param unicode friendly_name: Read only CompositionHook resources with friendly names that match this string
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.video.v1.composition_hook.CompositionHookInstance]
        """
        return list(self.stream(
            enabled=enabled,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            friendly_name=friendly_name,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, enabled=values.unset, date_created_after=values.unset,
             date_created_before=values.unset, friendly_name=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of CompositionHookInstance records from the API.
        Request is executed immediately

        :param bool enabled: Read only CompositionHook resources with an enabled value that matches this parameter
        :param datetime date_created_after: Read only CompositionHook resources created on or after this ISO 8601 datetime with time zone
        :param datetime date_created_before: Read only CompositionHook resources created before this ISO 8601 datetime with time zone
        :param unicode friendly_name: Read only CompositionHook resources with friendly names that match this string
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CompositionHookInstance
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookPage
        """
        params = values.of({
            'Enabled': enabled,
            'DateCreatedAfter': serialize.iso8601_datetime(date_created_after),
            'DateCreatedBefore': serialize.iso8601_datetime(date_created_before),
            'FriendlyName': friendly_name,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return CompositionHookPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of CompositionHookInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CompositionHookInstance
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return CompositionHookPage(self._version, response, self._solution)

    def create(self, friendly_name, enabled=values.unset, video_layout=values.unset,
               audio_sources=values.unset, audio_sources_excluded=values.unset,
               resolution=values.unset, format=values.unset,
               status_callback=values.unset, status_callback_method=values.unset,
               trim=values.unset):
        """
        Create a new CompositionHookInstance

        :param unicode friendly_name: A unique string to describe the resource
        :param bool enabled: Whether the composition hook is active
        :param dict video_layout: An object that describes the video layout of the composition hook
        :param unicode audio_sources: An array of track names from the same group room to merge
        :param unicode audio_sources_excluded: An array of track names to exclude
        :param unicode resolution: A string that describes the rows (width) and columns (height) of the generated composed video in pixels
        :param CompositionHookInstance.Format format: The container format of the media files used by the compositions created by the composition hook
        :param unicode status_callback: The URL we should call to send status information to your application
        :param unicode status_callback_method: The HTTP method we should use to call status_callback
        :param bool trim: Whether to clip the intervals where there is no active media in the Compositions triggered by the composition hook

        :returns: Newly created CompositionHookInstance
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'Enabled': enabled,
            'VideoLayout': serialize.object(video_layout),
            'AudioSources': serialize.map(audio_sources, lambda e: e),
            'AudioSourcesExcluded': serialize.map(audio_sources_excluded, lambda e: e),
            'Resolution': resolution,
            'Format': format,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
            'Trim': trim,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return CompositionHookInstance(self._version, payload, )

    def get(self, sid):
        """
        Constructs a CompositionHookContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.video.v1.composition_hook.CompositionHookContext
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookContext
        """
        return CompositionHookContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a CompositionHookContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.video.v1.composition_hook.CompositionHookContext
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookContext
        """
        return CompositionHookContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.CompositionHookList>'


class CompositionHookPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the CompositionHookPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.video.v1.composition_hook.CompositionHookPage
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookPage
        """
        super(CompositionHookPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CompositionHookInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.video.v1.composition_hook.CompositionHookInstance
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookInstance
        """
        return CompositionHookInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.CompositionHookPage>'


class CompositionHookContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, sid):
        """
        Initialize the CompositionHookContext

        :param Version version: Version that contains the resource
        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.video.v1.composition_hook.CompositionHookContext
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookContext
        """
        super(CompositionHookContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/CompositionHooks/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a CompositionHookInstance

        :returns: Fetched CompositionHookInstance
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return CompositionHookInstance(self._version, payload, sid=self._solution['sid'], )

    def delete(self):
        """
        Deletes the CompositionHookInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def update(self, friendly_name, enabled=values.unset, video_layout=values.unset,
               audio_sources=values.unset, audio_sources_excluded=values.unset,
               trim=values.unset, format=values.unset, resolution=values.unset,
               status_callback=values.unset, status_callback_method=values.unset):
        """
        Update the CompositionHookInstance

        :param unicode friendly_name: A unique string to describe the resource
        :param bool enabled: Whether the composition hook is active
        :param dict video_layout: A JSON object that describes the video layout of the composition hook
        :param unicode audio_sources: An array of track names from the same group room to merge
        :param unicode audio_sources_excluded: An array of track names to exclude
        :param bool trim: Whether to clip the intervals where there is no active media in the Compositions triggered by the composition hook
        :param CompositionHookInstance.Format format: The container format of the media files used by the compositions created by the composition hook
        :param unicode resolution: A string that describes the columns (width) and rows (height) of the generated composed video in pixels
        :param unicode status_callback: The URL we should call to send status information to your application
        :param unicode status_callback_method: The HTTP method we should use to call status_callback

        :returns: Updated CompositionHookInstance
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'Enabled': enabled,
            'VideoLayout': serialize.object(video_layout),
            'AudioSources': serialize.map(audio_sources, lambda e: e),
            'AudioSourcesExcluded': serialize.map(audio_sources_excluded, lambda e: e),
            'Trim': trim,
            'Format': format,
            'Resolution': resolution,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return CompositionHookInstance(self._version, payload, sid=self._solution['sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Video.V1.CompositionHookContext {}>'.format(context)


class CompositionHookInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    class Format(object):
        MP4 = "mp4"
        WEBM = "webm"

    def __init__(self, version, payload, sid=None):
        """
        Initialize the CompositionHookInstance

        :returns: twilio.rest.video.v1.composition_hook.CompositionHookInstance
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookInstance
        """
        super(CompositionHookInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'friendly_name': payload['friendly_name'],
            'enabled': payload['enabled'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'sid': payload['sid'],
            'audio_sources': payload['audio_sources'],
            'audio_sources_excluded': payload['audio_sources_excluded'],
            'video_layout': payload['video_layout'],
            'resolution': payload['resolution'],
            'trim': payload['trim'],
            'format': payload['format'],
            'status_callback': payload['status_callback'],
            'status_callback_method': payload['status_callback_method'],
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: CompositionHookContext for this CompositionHookInstance
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookContext
        """
        if self._context is None:
            self._context = CompositionHookContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def enabled(self):
        """
        :returns: Whether the CompositionHook is active
        :rtype: bool
        """
        return self._properties['enabled']

    @property
    def date_created(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def audio_sources(self):
        """
        :returns: The array of track names to include in the compositions created by the composition hook
        :rtype: unicode
        """
        return self._properties['audio_sources']

    @property
    def audio_sources_excluded(self):
        """
        :returns: The array of track names to exclude from the compositions created by the composition hook
        :rtype: unicode
        """
        return self._properties['audio_sources_excluded']

    @property
    def video_layout(self):
        """
        :returns: A JSON object that describes the video layout of the Composition
        :rtype: dict
        """
        return self._properties['video_layout']

    @property
    def resolution(self):
        """
        :returns: The dimensions of the video image in pixels expressed as columns (width) and rows (height)
        :rtype: unicode
        """
        return self._properties['resolution']

    @property
    def trim(self):
        """
        :returns: Whether intervals with no media are clipped
        :rtype: bool
        """
        return self._properties['trim']

    @property
    def format(self):
        """
        :returns: The container format of the media files used by the compositions created by the composition hook
        :rtype: CompositionHookInstance.Format
        """
        return self._properties['format']

    @property
    def status_callback(self):
        """
        :returns: The URL to send status information to your application
        :rtype: unicode
        """
        return self._properties['status_callback']

    @property
    def status_callback_method(self):
        """
        :returns: The HTTP method we should use to call status_callback
        :rtype: unicode
        """
        return self._properties['status_callback_method']

    @property
    def url(self):
        """
        :returns: The absolute URL of the resource
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a CompositionHookInstance

        :returns: Fetched CompositionHookInstance
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the CompositionHookInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def update(self, friendly_name, enabled=values.unset, video_layout=values.unset,
               audio_sources=values.unset, audio_sources_excluded=values.unset,
               trim=values.unset, format=values.unset, resolution=values.unset,
               status_callback=values.unset, status_callback_method=values.unset):
        """
        Update the CompositionHookInstance

        :param unicode friendly_name: A unique string to describe the resource
        :param bool enabled: Whether the composition hook is active
        :param dict video_layout: A JSON object that describes the video layout of the composition hook
        :param unicode audio_sources: An array of track names from the same group room to merge
        :param unicode audio_sources_excluded: An array of track names to exclude
        :param bool trim: Whether to clip the intervals where there is no active media in the Compositions triggered by the composition hook
        :param CompositionHookInstance.Format format: The container format of the media files used by the compositions created by the composition hook
        :param unicode resolution: A string that describes the columns (width) and rows (height) of the generated composed video in pixels
        :param unicode status_callback: The URL we should call to send status information to your application
        :param unicode status_callback_method: The HTTP method we should use to call status_callback

        :returns: Updated CompositionHookInstance
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookInstance
        """
        return self._proxy.update(
            friendly_name,
            enabled=enabled,
            video_layout=video_layout,
            audio_sources=audio_sources,
            audio_sources_excluded=audio_sources_excluded,
            trim=trim,
            format=format,
            resolution=resolution,
            status_callback=status_callback,
            status_callback_method=status_callback_method,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Video.V1.CompositionHookInstance {}>'.format(context)
