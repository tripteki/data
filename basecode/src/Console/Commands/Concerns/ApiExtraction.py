from ....Extraction.Api.Contracts.IApi import IApi

class ApiExtraction:

    def __call__ (self, extraction: IApi) -> None:
        """
        :type extraction: IApi
        :rtype: None
        """
        if isinstance (extraction, IApi):
            extraction.log ()
            extraction.parse ()
