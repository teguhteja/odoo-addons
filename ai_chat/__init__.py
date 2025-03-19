from . import controllers
import logging

_logger = logging.getLogger(__name__)

try:
    import openai # type: ignore[reportGeneralTypeIssues]
except ImportError:
    _logger.error("The 'openai' package is not installed. Please install it by running 'pip install openai'.")
    raise ImportError("The 'openai' package is not installed. Please install it by running 'pip install openai'.")

try:
    import semantic_kernel # type: ignore[reportGeneralTypeIssues]
except ImportError:
    _logger.error("The 'semantic_kernel' package is not installed. Please install it by running 'pip install semantic_kernel'.")
    raise ImportError("The 'semantic_kernel' package is not installed. Please install it by running 'pip install semantic_kernel'.")
