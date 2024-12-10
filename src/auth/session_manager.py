# COPYRIGHT © 2024 by Spring Health Corporation <office(at)springhealth.org>
# Toronto, Ontario, Canada
# SUMMARY: This file is part of the Get Well Clinic's original "AI-MOA" project's collection of software,
# documentation, and configuration files.
# These programs, documentation, and configuration files are made available to you as open source
# in the hopes that your clinic or organization may find it useful and improve your care to the public
# by reducing administrative burden for your staff and service providers.
# NO WARRANTY: This software and related documentation is provided "AS IS" and WITHOUT ANY WARRANTY of any kind;
# and WITHOUT EXPRESS OR IMPLIED WARRANTY OF SUITABILITY, MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.
# LICENSE: This software is licensed under the "GNU Affero General Public License Version 3".
# Please see LICENSE file for full details. Or contact the Free Software Foundation for more details.
# ***
# NOTICE: We hope that you will consider contributing to our common source code repository so that
# others may benefit from your shared work.
# However, if you distribute this code or serve this application to users in modified form,
# or as part of a derivative work, you are required to make your modified or derivative work
# source code available under the same herein described license.
# Please notify Spring Health Corp <office(at)springhealth.org> where your modified or derivative work
# source code can be acquired publicly in its latest most up-to-date version, within one month.
# ***

import logging
from config import ConfigManager
from .login_manager import LoginManager

logger = logging.getLogger(__name__)

class SessionManager:
    """
    A class for managing sessions in the AI MOA system.

    This class is responsible for creating and maintaining sessions,
    including handling the login process.

    Attributes:
        config (ConfigManager): An instance of ConfigManager containing
                                the configuration settings.
        login_manager (LoginManager): An instance of LoginManager for
                                      handling login operations.
        session: The current session object.
    """

    def __init__(self, config: ConfigManager):
        """
        Initialize the SessionManager with a configuration.

        This constructor creates a LoginManager instance and attempts
        to log in immediately upon creation.

        Args:
            config (ConfigManager): An instance of ConfigManager containing
                                    the configuration settings.
        """
        self.config = config
        self.login_manager = LoginManager(config)
        self.session, login_successful = self.login_manager.login_with_requests()
        if login_successful:
            logger.info("Login successful!")
        else:
            logger.error("Login failed.")
        logger.debug("SessionManager initialized")

    def login(self):
        """
        Attempt to log in and create a new session.

        Returns:
            bool: True if login was successful, False otherwise.
        """
        logger.info("Attempting to log in and create a new session")
        self.session, login_successful = self.login_manager.login_with_requests()
        return login_successful

    def get_session(self):
        """
        Get the current session object.

        Returns:
            The current session object.
        """
        logger.debug("Retrieving current session")
        return self.session
